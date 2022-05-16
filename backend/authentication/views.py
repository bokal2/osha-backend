from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import RegisterSerializer, LoginSerializer, EmailVerificationSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status, views
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
import jwt
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import User
from .utils import Util

# Create your views here.

class AuthUserAPIView(GenericAPIView):

    permission_classes = (IsAuthenticated,)
    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)

        return Response({'user': serializer.data})

class RegisterAPIView(GenericAPIView):

    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()

            user_data= serializer.data
            user = User.objects.get(email=user_data['email'])
            token = RefreshToken.for_user(user).access_token

            current_site = get_current_site(request).domain

            relativeLink = reverse('email-verify')
            absurl = "http://"+current_site+relativeLink+"?token="+str(token)
            email_data = '''
            Hi {0}, use the link below to verify your email address
            Link: {1}
            '''.format(user.email, absurl)

            data = { "email_body": email_data, "subject":"Verify your email", "user_email": user.email}
            Util.sendEmail(data)

            return Response(user_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VerifyEmail(views.APIView):

    serializer_class = EmailVerificationSerializer
    # token_param_config = openapi.Parameter('token',in_=openapi.IN_QUERY,description='Description',type=openapi.TYPE_STRING)

    #@swagger_auto_schema(manual_parameters=['token_param_config'])
    def get(self, request):
        token= request.GET.get('token')

        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
            user = User.objects.get(id=payload['user_id'])

            if not user.email_verified:
                user.email_verified = True
                user.save()

            return Response({'Account': 'Account verified successfully'}, status=status.HTTP_200_OK)

        except jwt.ExpiredSignatureError as ex:
            return Response({'error': 'Link expired'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as ex:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(GenericAPIView):

    serializer_class = LoginSerializer

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)




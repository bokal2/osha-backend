from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Agent
from .serializers import AgentSerializer

# Create your views here.

class AgentApiView(viewsets.ModelViewSet):
    serializer_class = AgentSerializer
    queryset = Agent.objects.all()
    # permission_classes = (IsAuthenticated,)
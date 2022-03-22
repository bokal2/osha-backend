from django.test import TestCase
from rest_framework.test import APITestCase

from authentication.models import User

# Create your tests here.

class TestModel(APITestCase):
    
    def test_raise_error_no_username(self):
        self.assertRaises(ValueError, User.objects.create_user,username="", email="okalbob@gmail.com", password="Abcd@1234")
    def test_raise_error_no_email(self):
        self.assertRaises(ValueError, User.objects.create_user,username="eokal", email="", password="Abcd@1234")
    def test_create_user(self):
        user = User.objects.create_user('eokal','okalbob@gmail.com', 'Abcd@1234')
        self.assertIsInstance(user, User)
        self.assertFalse(user.is_staff)
        self.assertEqual(user.email, 'okalbob@gmail.com')
    def test_create_superuser_with_staff_status(self):
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_staff=True.'):
            User.objects.create_superuser(username='eokal',email='okalbob@gmail.com', password='Abcd@1234', is_staff=False)
    def test_create_superuser_with_superuser_status(self):
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_superuser=True.'):
            User.objects.create_superuser(username='eokal',email='okalbob@gmail.com', password='Abcd@1234', is_superuser=False)
    def test_create_superuser(self):
        user = User.objects.create_superuser('eokal','okalbob@gmail.com', 'Abcd@1234')
        self.assertIsInstance(user, User)
        self.assertTrue(user.is_staff)
        self.assertEqual(user.email, 'okalbob@gmail.com')
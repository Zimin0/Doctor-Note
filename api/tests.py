from django.test import TestCase, Client
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

class LoginTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='admin', password='admin')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

    def test_login(self):
        data = {
            'username': 'admin',
            'password' : 'admin'
        }
        response = self.client.post('/api/login/', data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('token', response.data) # Проверяем, что в ответе есть токен

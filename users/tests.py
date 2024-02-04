from django.test import TestCase, Client
from django.contrib.auth.models import User

class LoginAndLogoutTestCase(TestCase):
    """ Проверка системы регистрации. """
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='admin',
            email='admin@gmail.com',
            password='admin'
        )
    
    def test_login_and_get_doctors_page(self):
        """ Можно ли получить страницу докторов, войдя в систему. """
        self.client.login(username='admin', password='admin')
        response = self.client.get('/welcome/', follow=True)
        self.assertEqual(len(response.redirect_chain), 0)
        # print(response.headers)
        # print(response.content)
        # r = response.templates[0]
        # print(r)
        # print(r.name. r.origin, r.engine, r.source)
        # print(response.content.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
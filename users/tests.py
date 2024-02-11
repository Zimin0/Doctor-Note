from django.test import TestCase, Client
from django.contrib.auth.models import User

class LoginAndLogoutTestCase(TestCase):
    """ Проверка системы регистрации. """
    def setUp(self):
        self.user = User.objects.create_user(
            username='admin',
            email='admin@gmail.com',
            password='admin'
        )
        self.client.login(username='admin', password='admin')
    
    def test_login_and_get_doctors_page(self):
        """ Можно ли получить страницу докторов, войдя в систему. """
        response = self.client.get('/doctors/', follow=True)
        self.assertEqual(len(response.redirect_chain), 0)
        self.assertEqual(response.status_code, 200)
        # print(response.headers)
        # print(response.content)
        # r = response.templates[0]
        # print(r)
        # print(r.name. r.origin, r.engine, r.source)
        # print(response.content.decode('utf-8'))
    
    def test_login_and_change_data_on_profile_page(self):
        """ Можно ли изменить данные пользователя, войдя в систему. """
        data = {"first_name": "Никита",
                "last_name": "Зименков",
                "email": "nik@gmail.com",
                "need_to_send_notifics_on_mail": True
                }
        response = self.client.post('/users/profile/', data)
        updated_user = User.objects.get(id=self.user.id)
        self.assertEqual(updated_user.profile.need_to_send_notifics_on_mail, True)
        self.assertEqual(updated_user.first_name, "Никита")
        self.assertEqual(updated_user.last_name, "Зименков")
        self.assertEqual(response.status_code, 201)
    
    def test_login_and_change_invalid_data_on_profile_page(self):
        """ Проверка валидации почты в форме изменения в профиле. """
        data = {"first_name": "Никита",
                "last_name": "Зименков",
                "email": "nikgmailcom",
                }
        response = self.client.post('/users/profile/', data)
        self.assertEqual(response.status_code, 400)
    
    

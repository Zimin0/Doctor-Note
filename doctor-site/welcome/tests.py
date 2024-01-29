from django.test import TestCase, Client

class LoginSystemTestCase(TestCase):
    """ Проверка редиректа незарегистрированного пользователя на страницу welcome """
    def setUp(self):
        self.client = Client()

    def test_check_redirected__page_status_doctors(self):
        response = self.client.get('/doctors/', follow=True)
        redirect_status = response.redirect_chain[0][1]
        self.assertEqual(redirect_status, 302)

    def test_check_redirected__page_status_medicine(self):
        response = self.client.get('/medicine/', follow=True)
        redirect_status = response.redirect_chain[0][1]
        self.assertEqual(redirect_status, 302)
    
    def test_welcome_page_after_redirect_doctors(self):
        response = self.client.get('/doctors/', follow=True)
        redirect_page = response.redirect_chain[0][0].split('/') # [('/welcome/?next=/doctors/', 302)]
        self.assertEqual(redirect_page[1], 'welcome')
        self.assertEqual(redirect_page[3], 'doctors')
    
    def test_welcome_page_after_redirect_medicine(self):
        response = self.client.get('/medicine/', follow=True)
        redirect_page = response.redirect_chain[0][0].split('/') # [('/welcome/?next=/doctors/', 302)]
        self.assertEqual(redirect_page[1], 'welcome')
        self.assertEqual(redirect_page[3], 'medicine')


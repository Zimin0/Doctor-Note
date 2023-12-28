from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User

# is_report_was_added, is_appointment_over

class DoctorsAvailabilityTest(TestCase):
    """ Проверяет, возможно ли зарегестрированному пользователю получить доступ к страницам сайта. """
    def setUp(self):
        # self.client = Client() # Можно не создавать 
        self.user = User.objects.create_user('admin', 'admin@gmail.com', 'admin')
        self.client.login(username='admin', password='admin')

    def test_valid_status_code(self):
        response = self.client.get('/doctors/')
        self.assertEqual(response.status_code, 200)
    
    def test_needed_template_was_used(self):
        response = self.client.get('/doctors/')
        self.assertEqual(response.templates[0].name, 'doctors_appointment/doctors.html')

    def tearDown(self):
        ...
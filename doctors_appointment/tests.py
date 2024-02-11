from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User

from doctors_appointment.models import Appointment

import datetime
from django.utils import timezone


class DoctorsAvailabilityTest(TestCase):
    """ Проверяет, возможно ли зарегестрированному пользователю получить доступ к страницам сайта. """
    def setUp(self):
        # self.client = Client() # Можно не создавать # Every test case in a django.test.*TestCase instance has access to an instance of a Django test client. This client can be accessed as self.client. This client is recreated for each test, so you don’t have to worry about state (such as cookies) carrying over from one test to another.
        self.user = User.objects.create_user('admin', 'admin@gmail.com', 'admin')
        self.client.login(username='admin', password='admin')

    def test_valid_status_code(self):
        """ Страница /doctors/ загружается. """
        response = self.client.get('/doctors/')
        self.assertEqual(response.status_code, 200)
    
    def test_needed_template_was_used(self):
        """ На странице /doctors/ используется doctors.html. """
        response = self.client.get('/doctors/')
        self.assertEqual(response.templates[0].name, 'doctors_appointment/doctors.html')

    def test_create_doctor_appoint(self):
        """ Можно ли создать новую запись к врачу. """
        date = timezone.now().date() + datetime.timedelta(days=1)
        time = timezone.now().time().strftime('%H:%M')
        appointment = {
            'doctor': 'Тестовый_врач',
            'date': date,
            'time': time,
            'address': 'Тестовый адрес, д. 0',
            'office_number': "101",
            'health_troubles': "Тестовые жалобы",
            'report': "",
            'is_ended': False,
            'archived': False,
        }
        response = self.client.post('/doctors/add/', appointment, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.redirect_chain[0][0], '/doctors/')
        self.assertTrue(Appointment.active_appointments_sorted.filter(doctor='Тестовый_врач'))

    def tearDown(self):
        ...
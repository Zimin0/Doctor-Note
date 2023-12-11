from django.urls import path

from medicine.views import display_medicines, add_medicine, edit_medicine

app_name = 'medicine'

urlpatterns = [
    path('', display_medicines, name='display_medicines'),
    path('add/', add_medicine, name='add_medicine'),
    path('edit/<int:medicine_id>/', edit_medicine, name='edit_medicine'),
]
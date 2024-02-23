from doctors_appointment.models import Appointment

from rest_framework import serializers

class AppointmentSerializer(serializers.ModelSerializer):
    # Для того, чтобы в ответе пациент оправлялся в виде ссылки, а не его pk 
    patient = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)
    class Meta:
        model = Appointment
        fields = '__all__'


"""  

view_name='user-detail' потому что отображаться будет модель USER
basename = 'user' - маршруты будут форматироваться в виде '<basename>-detail' - как пример
Укажите view_name, соответствующий имени маршрута, сгенерированного для детального просмотра записей модели Appointment. Если вы используете DefaultRouter, имя маршрута обычно формируется автоматически и имеет формат <model_name>-detail, где <model_name> — это имя модели в нижнем регистре.
Для модели Appointment view_name будет appointment-detail (если вы не задали кастомное basename при регистрации ViewSet):
"""
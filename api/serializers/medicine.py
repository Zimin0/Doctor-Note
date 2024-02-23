from medicine.models import Medicine

from rest_framework import serializers

class MedicineSerializer(serializers.ModelSerializer):
    patient = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)
    class Meta:
        model = Medicine
        fields = '__all__'

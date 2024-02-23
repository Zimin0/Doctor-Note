from rest_framework import serializers
from django.contrib.auth.models import User, Group

from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user
    
    def update(self, instance, validated_data):
        instance.username=validated_data.get('username', instance.username)
        instance.email=validated_data.get('email', instance.email)
        instance.save()
        return instance
    
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups', 'password']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
        
    
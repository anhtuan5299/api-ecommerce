from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import authentication_classes, permission_classes

from .models import CustomUser

class UserSerializer(serializers.HyperlinkedModelSerializer):

    def create(self, validation_data):
        password = validation_data.pop('password', None)
        instance = self.Meta.model(**validation_data)

        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validation_data):
        for attr, value in validation_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)

    class Meta:
        model = CustomUser
        extra_kwargs = {'password': {'write_only': True}}
        fields = ['name', 'email', 'password', 'phone', 'gender',
         'is_active', 'is_staff', 'is_superuser']
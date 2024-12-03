from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from .models import *

class OrganisationSerializer(ModelSerializer):
    class Meta:
        model = Organisation
        fields = ['id', 'name']

class ProfileSerializer(ModelSerializer):
    org = PrimaryKeyRelatedField(queryset=Organisation.objects.all())

    class Meta:
        model = Profile
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'org', 'employee_id', 'is_company_admin', 'phone_number', 'password']
        extra_kwargs = {
            'password' : {
                'write_only': True
            }
        }
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = super().create(validated_data)
        if password:
            instance.set_password(password)
            instance.save()
        return instance

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        instance = super().update(instance, validated_data)
        if password:
            instance.set_password(password)
            instance.save()
        return instance
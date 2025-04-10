from rest_framework import serializers
from core.models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

    def validate_email(self, value):
        if Doctor.objects.filter(email=value).exists():
            raise serializers.ValidationError("A doctor with this email already exists.")
        return value

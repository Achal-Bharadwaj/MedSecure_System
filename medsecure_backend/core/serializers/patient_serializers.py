from rest_framework import serializers
from core.models import Patient

class PatientSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')

    class Meta:
        model = Patient
        fields = '__all__'

    def validate_age(self, value):
        if value < 0:
            raise serializers.ValidationError("Age must be a positive number.")
        return value

    def validate_gender(self, value):
        valid = ['Male', 'Female', 'Other']
        if value not in valid:
            raise serializers.ValidationError("Gender must be one of: Male, Female, Other.")
        return value

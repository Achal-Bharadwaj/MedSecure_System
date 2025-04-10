from rest_framework import serializers
from core.models import PatientDoctorMapping

class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    patient_name = serializers.ReadOnlyField(source='patient.name')
    doctor_name = serializers.ReadOnlyField(source='doctor.name')

    class Meta:
        model = PatientDoctorMapping
        fields = '__all__'


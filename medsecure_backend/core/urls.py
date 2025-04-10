from django.urls import path
from core.views.auth_views import RegisterView
from core.views.doctor_views import DoctorListCreateView, DoctorRetrieveUpdateDeleteView
from core.views.patient_views import PatientListCreateView, PatientRetrieveUpdateDeleteView
from core.views.mapping_views import MappingListCreateView, MappingByPatientView, MappingDeleteView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # Auth
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='login'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Doctors
    path('doctors/', DoctorListCreateView.as_view(), name='doctor-list-create'),
    path('doctors/<int:pk>/', DoctorRetrieveUpdateDeleteView.as_view(), name='doctor-detail'),

    # Patients
    path('patients/', PatientListCreateView.as_view(), name='patient-list-create'),
    path('patients/<int:pk>/', PatientRetrieveUpdateDeleteView.as_view(), name='patient-detail'),

    # Mappings
    path('mappings/', MappingListCreateView.as_view(), name='mapping-list-create'),
    path('mappings/<int:patient_id>/', MappingByPatientView.as_view(), name='mapping-by-patient'),
    path('mappings/delete/<int:pk>/', MappingDeleteView.as_view(), name='mapping-delete'),
]

from django.urls import path
from .views import LandingAPIView

urlpatterns = [
    path('', LandingAPIView.as_view(), name='landing'),
]

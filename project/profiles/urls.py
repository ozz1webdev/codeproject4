from django.urls import path
from .views import Profiles

urlpatterns = [
    path('profiles/<slug:pk>/', Profiles.as_view(), name='profile'),
]

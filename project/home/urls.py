from django.urls import path
from .views import addPost, home, Dashboard

urlpatterns = [
    path('add/', addPost.as_view(), name='addPost'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('', home.as_view(), name='home'),
]

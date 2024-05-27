from django.urls import path
from .views import addPost, home

urlpatterns = [
    path('add/', addPost.as_view(), name='addPost'),
    path('', home.as_view(), name='home'),
]

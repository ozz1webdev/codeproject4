from django.urls import path
from . import views as homeViews

urlpatterns = [
    path('', homeViews.home.as_view(), name='home'),
]

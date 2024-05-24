from django.shortcuts import render
from django.views.generic import TemplateView, ListView
# Create your views here.


class home(TemplateView):
    template_name = 'home/home.html'

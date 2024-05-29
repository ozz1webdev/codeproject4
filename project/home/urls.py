from django.urls import path
from .views import addPost, home, postView

urlpatterns = [
    path('add/', addPost.as_view(), name='addPost'),
    path('postView/<slug:pk>/', postView.as_view(), name='postView'),
    path('', home.as_view(), name='home'),
]

from django.urls import path
from .views import addPost, home, postView, DeletePost, EditPost

urlpatterns = [
    path('add/', addPost.as_view(), name='addPost'),
    path('postView/<slug:pk>/', postView.as_view(), name='postView'),
    path('delete/<slug:pk>/', DeletePost.as_view(), name='deletePost'),
    path('edit/<slug:pk>/', EditPost.as_view(), name='editPost'),
    path('', home.as_view(), name='home'),
]

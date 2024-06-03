from django.urls import path
from .views import (addPost, about, home, postView,
                    postView2, DeletePost, EditPost,
                    PostLike)

urlpatterns = [
    path('add/', addPost.as_view(), name='addPost'),
    path('about/', about.as_view(), name='about'),
    path('postView/<slug:pk>/', postView.as_view(), name='postView'),
    path('postView2/<slug:pk>/', postView2.as_view(), name='postView2'),
    path('delete/<slug:pk>/', DeletePost.as_view(), name='deletePost'),
    path('edit/<slug:pk>/', EditPost.as_view(), name='editPost'),
    path('like/<slug:pk>/', PostLike.as_view(), name='post_like'),
    path('', home.as_view(), name='home'),
]

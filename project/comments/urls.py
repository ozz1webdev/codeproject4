from django.urls import path
from .views import (Comments, AddComment,
                    DeleteComment, EditComment)

urlpatterns = [
    path('<slug:pk>/', Comments.as_view(), name='comments'),
    path('addcomment/<slug:pk>/', AddComment.as_view(), name='addComment'),
    path('deletecomment/<slug:pk>/', DeleteComment.as_view(), name='deleteComment'),
    path('editcomment/<slug:pk>/', EditComment.as_view(), name='editComment'),
]

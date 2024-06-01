from django import forms
from .models import Post
from django.contrib import admin
from django_summernote.widgets import SummernoteWidget


# class CommentAdmin(admin.ModelAdmin):
#    list_display = ('name', 'post', 'body', 'created_on')
#    list_filter = ('name', 'created_on')
#    search_fields = ('name', 'body', 'email')


class CreatePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'image',
            'image_alt',
            'video',
            ]

        content = forms.CharField(widget=SummernoteWidget())

        widget = {
            # 'content': SummernoteWidget()
            'content': SummernoteWidget()
        }

        labels = {
            'title': 'Title',
            'content': 'Content',
            'image': 'Image',
            'image_alt': 'Image Alt',
            'video': 'Embed Youtube Link'
        }

from django import forms
from .models import Post
from django_summernote.widgets import SummernoteWidget


class CreatePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'image',
            'youtube_link'
            ]

        content = forms.CharField(widget=SummernoteWidget())

        widget = {
            'content': SummernoteWidget()
        }

        labels = {
            'title': 'Title',
            'content': 'Content',
            'image': 'Image',
            'youtube_link': 'Share Youtube Link'
        }

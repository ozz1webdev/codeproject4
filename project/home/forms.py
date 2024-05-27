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
            'video',
            ]

        content = forms.CharField(widget=SummernoteWidget())

        widget = {
            'content': SummernoteWidget()
        }

        labels = {
            'title': 'Title',
            'content': 'Content',
            'image': 'Image',
            'video': 'Embed Youtube Link'
        }

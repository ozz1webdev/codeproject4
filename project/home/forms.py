from django import forms
from .models import Post
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


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
            'content': SummernoteInplaceWidget()
        }

        labels = {
            'title': 'Title',
            'content': 'Content',
            'image': 'Image',
            'image_alt': 'Image Alt',
            'video': 'Embed Youtube Link'
        }

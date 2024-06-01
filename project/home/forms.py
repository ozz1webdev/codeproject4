from django import forms
from .models import Post, Comment
from django_summernote.widgets import SummernoteWidget


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


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body',]
        labels = {
            'body': 'Comment'
        }

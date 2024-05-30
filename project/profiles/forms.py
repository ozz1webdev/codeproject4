from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    """Form to Create profile"""
    class Meta:
        model = Profile
        fields = ['image', 'bio']

        labels = {
            'image': 'Profile Picture',
            'bio': 'Bio',
        }

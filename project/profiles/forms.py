from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    """Form to Create profile"""
    class Meta:
        model = Profile
        fields = ['image', 'name', 'lastname', 'bio',
                  'location', 'hobbys']

        labels = {
            'image': 'Profile Picture',
            'bio': 'Bio',
            'name': 'Name',
            'lastname': 'Lastname',
            'location': 'Location',
            'hobbys': 'Hobbys',
        }

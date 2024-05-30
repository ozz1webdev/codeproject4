from django.contrib import admin
from .models import Profile

# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'image', 'bio', 'name', 'lastname',
                    'birthdate', 'location', 'joined_on', 'hobbys')


admin.site.register(Profile, ProfileAdmin)

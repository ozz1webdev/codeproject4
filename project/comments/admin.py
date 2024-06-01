from django.contrib import admin
from .models import Comments
# Register your models here.


@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'body', 'created_on')
    list_filter = ('name', 'created_on')
    search_fields = ('name', 'body', 'email')

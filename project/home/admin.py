from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Friends

# Register your models here.


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('user', 'title', 'created_on', 'updated_at')
    list_filter = ('user', 'created_on', 'updated_at')
    search_fields = ('title', 'content')
    summernote_fields = ('content',)


@admin.register(Friends)
class FriendsAdmin(admin.ModelAdmin):
    list_display = ('user', 'friend')
    list_filter = ('user', 'friend')
    search_fields = ('user', 'friend')

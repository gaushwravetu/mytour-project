from django.contrib import admin
from .models import Post
from django.utils.html import format_html
# Register your models here.
@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="60" style="border-radius:50px;"/>'.format(object.place_photo.url))
    list_display = ('id', 'thumbnail', 'title', 'short_desc', 'location','author')
    list_display_links = ('id','thumbnail','title')

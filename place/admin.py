from django.contrib import admin
from .models import Place
from django.utils.html import format_html
# Register your models here.
class PlaceAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="60" style="border-radius:50px;"/>'.format(object.place_photo.url))
    thumbnail.short_description = 'Place Image'
    list_display = ('id','thumbnail','place_title','country','location','architecture','sea_level','no_of_visitors','is_trending','is_recommended')
    list_display_links = ('id','thumbnail','place_title')
    search_fields = ('place_title','id','location','country')
    list_filter = ('location','country','architecture','is_trending','is_recommended')
admin.site.register(Place,PlaceAdmin)
from django.db import models
from datetime import datetime
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length=100, default=' ')
    title = models.CharField(max_length=150)
    user_id = models.IntegerField(blank=True)
    location = models.CharField(max_length=100, default=' ')
    short_desc = models.CharField(max_length=500, default=' ')
    full_desc = RichTextUploadingField(default=' ')
    place_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    added_date = models.DateTimeField(default=datetime.now,blank=True)
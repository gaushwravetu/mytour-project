from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
# Create your models here.
class Place(models.Model):
    place_title = models.CharField(max_length=255)
    country = models.CharField(max_length=100,default=' ')
    location = models.CharField(max_length=100,default=' ')
    description = RichTextField()
    place_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    place_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    place_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    place_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    place_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_trending = models.BooleanField(default=False)
    is_recommended = models.BooleanField(default=False)
    one_strong_point_for_recommendations = models.CharField(max_length=100,default='In 2-3 words',blank='True')
    architecture = models.CharField(max_length=100)
    feature1 = models.CharField(max_length=100,default=' ')
    feature2 = models.CharField(max_length=100,default=' ')
    feature3 = models.CharField(max_length=100,default=' ')
    feature4 = models.CharField(max_length=100,default=' ')
    feature5 = models.CharField(max_length=100,default=' ')
    Explain_each_feature = RichTextField(default=' ')
    Reasons_to_visit = RichTextField(default=' ')
    story1 = RichTextField(default=' ')
    story2 = RichTextField(default=' ')
    story3 = RichTextField(default=' ')
    story4 = RichTextField(default=' ')
    Max_temperature = models.CharField(max_length=100,default='in ℃')
    Min_temperature = models.CharField(max_length=100,default='in ℃')
    sea_level = models.CharField(max_length=10000)
    no_of_visitors = models.CharField(max_length=1000000,default='1000')
    closeness_of_the_destination = RichTextField()
    added_date = models.DateTimeField(default=datetime.now,blank=True)
    
    def __str__(self):
        return self.place_title
    
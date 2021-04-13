from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
# Create your models here.
class Place(models.Model):
    country_choice = (
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('DC', 'District Of Columbia'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming'),
    )
    place_title = models.CharField(max_length=255)
    country = models.CharField(choices=country_choice,max_length=100)
    location = models.CharField(max_length=100,default='Agra')
    description = RichTextField()
    place_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    place_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    place_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    place_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    place_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_trending = models.BooleanField(default=False)
    is_recommended = models.BooleanField(default=False)
    architecture = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100,default='like: extensive use of marble')
    sea_level = models.CharField(max_length=10000)
    closeness_of_the_destination = RichTextField()
    added_date = models.DateTimeField(default=datetime.now,blank=True)
    
    def __str__(self):
        return self.place_title
    
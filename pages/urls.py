from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('community',views.community,name='community'),
    path('places',views.places,name='places'),
    path('contact',views.contact,name='contact')
]
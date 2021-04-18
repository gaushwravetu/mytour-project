from django.urls import path
from . import views
urlpatterns = [
    path('',views.place,name='place'),
    path('<int:id>',views.place_detail,name='place_detail'),
    path('search',views.search, name='search'),
]
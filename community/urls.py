from django.urls import path
from . import views
urlpatterns = [
    path('',views.community,name='community'),
    path('<int:id>',views.community_detail,name='community_detail'),
    path('addpost',views.add_post,name='addpost'),
    path('delete/<int:id>',views.delete_post,name='deletepost'),
    path('searchpost',views.search_post,name='searchpost'),
]
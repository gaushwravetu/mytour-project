from django.shortcuts import render
from pages.models import Team
from place.models import Place
# Create your views here.
def home(request):
    teams = Team.objects.all()
    trending_place = Place.objects.order_by('-added_date').filter(is_trending=True)
    recommended_place = Place.objects.order_by('-added_date').filter(is_recommended=True)
    data = {'teams': teams, 'recommended_place':recommended_place, 'trending_place':trending_place}
    return render(request,'pages/home.html',data)

def about(request):
    teams = Team.objects.all()
    data = {'teams':teams}
    return render(request,'pages/about.html',data)

def community(request):
    return render(request,'pages/community.html')
    
    
def contact(request):
    return render(request,'pages/contact.html')
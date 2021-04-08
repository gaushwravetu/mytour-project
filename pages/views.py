from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'pages/home.html')

def about(request):
    return render(request,'pages/about.html')

def community(request):
    return render(request,'pages/community.html')

def places(request):
    return render(request,'pages/places.html')

def contact(request):
    return render(request,'pages/contact.html')
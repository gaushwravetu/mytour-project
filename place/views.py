from django.shortcuts import render, get_object_or_404
from .models import Place
# Create your views here.
def place(request):
    return render(request,'place/place.html')

def place_detail(request, id):
    single_place = get_object_or_404(Place,pk=id)

    data = {
        'single_place': single_place,
    }
    return render(request,'place/place_detail.html',data)
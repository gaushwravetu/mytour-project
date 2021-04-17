from django.shortcuts import render, get_object_or_404
from .models import Place
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.
def place(request):
    places = Place.objects.order_by('-added_date')
    paginator = Paginator(places,4)
    page = request.GET.get('page')
    paged_places = paginator.get_page(page)
    data = {
        'places': paged_places,
    }
    return render(request,'place/place.html',data)

def place_detail(request, id):
    single_place = get_object_or_404(Place,pk=id)

    data = {
        'single_place': single_place,
    }
    return render(request,'place/place_detail.html',data)
from django.shortcuts import render, get_object_or_404
from .models import Place
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.
def place(request):
    places = Place.objects.order_by('-added_date')
    paginator = Paginator(places,10)
    page = request.GET.get('page')
    paged_places = paginator.get_page(page)
    country_search = Place.objects.values_list('country',flat=True).distinct()
    location_search = Place.objects.values_list('location',flat=True).distinct()
    architecture_search = Place.objects.values_list('architecture',flat=True).distinct()
    data = {
        'places': paged_places,
        'country_search':country_search,
        'location_search': location_search,
        'architecture_search': architecture_search,
    }
    return render(request,'place/place.html',data)

def place_detail(request, id):
    single_place = get_object_or_404(Place,pk=id)
    single_place.views = single_place.views + 1
    single_place.save()

    data = {
        'single_place': single_place,
    }
    return render(request,'place/place_detail.html',data)

def search(request):
    places = Place.objects.order_by('-added_date')
    country_search = Place.objects.values_list('country',flat=True).distinct()
    location_search = Place.objects.values_list('location',flat=True).distinct()
    architecture_search = Place.objects.values_list('architecture',flat=True).distinct()
    # search for keyword in places if not found then it will search inside description and show the results
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            places = places.filter(description__icontains=keyword)
    if 'country' in request.GET:
        country = request.GET['country']
        if country:
            places = places.filter(country__iexact=country)
    if 'location' in request.GET:
        location = request.GET['location']
        if location:
            places = places.filter(location__iexact=location)
    if 'architecture' in request.GET:
        architecture = request.GET['architecture']
        if architecture:
            places = places.filter(architecture__iexact=architecture)

    data = {
        'places': places,
        'country_search':country_search,
        'location_search': location_search,
        'architecture_search': architecture_search,
    }
    return render(request,'place/search.html',data)
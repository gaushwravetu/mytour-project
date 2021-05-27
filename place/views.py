from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q

# Create your views here.

def place(request):
    places = Place.objects.order_by('-added_date')
    paginator = Paginator(places,9)
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

    # Tracking IP Address
    # def get_client_ip(request):
    #     address = request.META.get('HTTP_X_FORWARDED_FOR')
    #     if address:
    #         ip = address.split(',')[-1].strip()
    #     else:
    #         ip = request.META.get('REMOTE_ADDR')
    #     return ip
    # ip = get_client_ip(request)
    # find_ip = Place.objects.filter(Q(views__icontains=ip))
    # if len(find_ip)<1:
    #     add_ip = Place(views=ip)
    #     add_ip.save()
    # count = single_place.views.all().count()
    # single_place.views_count.add(count)

    




    single_place.place_views = single_place.place_views + 1
    single_place.save()

    # def get(self, request, *args, **kwargs):
    #     ip = get_client_ip(self.request)
    #     if IpModel.objects.filter(ip=ip).exists():
    #         place_id = request.GET.get('place-id')
    #         place = Place.objects.get(pk=place_id)
    #         place.views.add(IpModel.objects.get(ip=ip))
    #     else:
    #         IpModel.objects.create(ip=ip)
    #         place_id = request.GET.get('place-id')
    #         place = Place.objects.get(pk=place_id)
    #         place.views.add(IpModel.objects.get(ip=ip))

    data = {
        'single_place': single_place,
        # 'count':count,
    }
    return render(request,'place/place_detail.html',data)

def search(request):
    places = Place.objects.order_by('-added_date')
    top_place = (Place.objects
                    .order_by('-place_views')
                    .values_list('place_views',flat=True)
                    )
    top_records = (Place.objects
                        .order_by('-place_views')
                        .filter(place_views__in=top_place[:3]))
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
        # 'top_records': top_records,
        'places': places,
        'country_search':country_search,
        'location_search': location_search,
        'architecture_search': architecture_search,
    }
    return render(request,'place/search.html',data)
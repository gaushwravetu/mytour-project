from django.shortcuts import render,get_object_or_404, redirect
from .models import Post
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import PostForm
from django.utils.datastructures import MultiValueDictKeyError
# Create your views here.

def error_404_view(request,exception):
    return render(request,'community/404.html')

def community(request):
    post_page = Post.objects.order_by('-added_date')
    location_search = Post.objects.values_list('location',flat=True).distinct()
    posts = Post.objects.all()
    paginator = Paginator(post_page,3)
    page = request.GET.get('page')
    paged_posts = paginator.get_page(page)
    if 'location' in request.GET:
        location = request.GET['location']
        if location:
            posts = posts.filter(location__iexact=location)
    data = {
        'post_page': paged_posts,
        'posts': posts,
        'location_search':location_search,
    }
    
    return render(request,'community/community.html',data)

def community_detail(request, id):
    single_post = get_object_or_404(Post,pk=id)

    data = {
        'single_post': single_post,
    }
    return render(request,'community/community_detail.html',data)

def search_post(request):
    # posts = Post.objects.order_by('-added_date')
    # location_search = Post.objects.values_list('location',flat=True).distinct()
    keyword = request.GET['keyword']
    if len(keyword) > 78:
        posts = Post.objects.none()
    else:
        posts_desc = Post.objects.filter(full_desc__icontains=keyword)
        posts_sdesc = Post.objects.filter(short_desc__icontains=keyword)
        posts_title = Post.objects.filter(title__icontains=keyword)
        posts_location = Post.objects.filter(location__icontains=keyword)
        posts = posts_desc.union(posts_title,posts_location,posts_sdesc)

    # if 'keyword' in request.GET:
    #     keyword = request.GET['keyword']
    #     if keyword:
    #         posts = posts.filter(full_desc__icontains=keyword)
            
    # if 'location' in request.GET:
    #     location = request.GET['location']
    #     if location:
    #         posts = posts.filter(location__iexact=location)
    data = {
        'posts':posts,
        'keyword':keyword
    }
    return render(request,'community/searchpost.html',data)

@login_required(login_url = 'login')
def add_post(request):
    if request.method == "POST":
        try:
            is_private = request.POST['is_private']
        except MultiValueDictKeyError:
            is_private = False
        author = request.POST['author']
        title = request.POST['title']
        user_id = request.POST.get('user_id')
        location = request.POST['location']
        short_desc = request.POST['short_desc']
        full_desc = request.POST['full_desc']
        place_photo = request.FILES.get('place_photo')
        post = Post(author=author, user_id=user_id, title=title, location=location,
        short_desc=short_desc,full_desc=full_desc, place_photo=place_photo)
        post.save()
        messages.success(request,"Your post uploaded successfully")


    #added for forms
    # if request.method == "POST":
    #     form = PostForm(request.POST)
    #     if form.is_valid():
    #         post = form.save(commit=False)
    #         post.save()
    #         form = PostForm()
    #         messages.success(request,"Your post uploaded successfully")
    #         return redirect('community/addpost.html')
    # else:
    #     form = PostForm()
    # return render(request,'community/addpost.html',{'form':form})



    # if request.method == "POST":
    #     form = PostForm(request.POST)
    #     print(request.POST)
    #     if form.is_valid():
    #         author = request.POST['author']
    #         title = request.POST['title']
    #         user_id = request.POST['user_id']
    #         location = request.POST['location']
    #         short_desc = request.POST['short_desc']
    #         full_desc = request.POST['full_desc']
    #         place_photo = request.POST['place_photo']
    #         post = Post(author=author, user_id=user_id, title=title, location=location,
    #         short_desc=short_desc,full_desc=full_desc,place_photo=place_photo)
    #         post.save()
    #         form = PostForm()
    #         messages.success(request,"Your post uploaded successfully")
    #         return redirect('community/addpost.html')
    # else:
    #     form = PostForm()
    return render(request,'community/addpost.html')



# @login_required(login_url = 'login')
# def update_post(request, id):
#     if request.method == "POST":
#         post = get_object_or_404(Post,pk=id)
#         post.save()
#         messages.success(request,"Your post updated successfully")
#     post = get_object_or_404(Post,pk=id)
#     data = {
#         'post': post,
#     }
#     return render(request,'community/updatepost.html',data)
    
    

@login_required(login_url = 'login')
def delete_post(request, id):
    if request.method == "POST":
        post = Post.objects.get(pk=id)
        post.delete()
        messages.success(request,"Your post deleted successfully")
    return redirect('dashboard')

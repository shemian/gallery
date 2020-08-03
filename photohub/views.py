from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
from .models import Image,Location,Category

# Create your views here.

def index(request):
    images = Image.objects.all()
    locations = Location.get_location()
    categorys = Category.get_category()
    print(locations)
    print(categorys)
    return render(request,'index.html',{'images':images[::-1],'locations':locations,'categorys':categorys})

def image_location(request, location):
    image = Image.filter_by_location(loactions)
    print(images)
    return render(request,'location.html',{'location_images': images})

def image_category(request, category):
    images = Image.filter_by_category(category)
    print(images)
    return render(request,'category.html',{'category_images':images})

def search_results(request):
    if 'imagesearch' in request.GET and request.GET["imagesearch"]:
        category = request.GET.get("imagesearch")
        searched_images = Image.search_by_category(category)
        message = f"{category}"
        print(searched_images)
        return render(request, 'search_results.html', {"message": message,"category":category, "images": searched_images})
    else:
        message = "You haven't searched for any image category"
        return render(request, 'search_results.html', {"message": message,"category":category})

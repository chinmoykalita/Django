from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image

# Create your views here.

def welcome(request):

    photos=Image.objects.all()
    return render(request, 'all-photos/welcome.html', {"photos":photos})




def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'all-photos/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html',{"message":message})




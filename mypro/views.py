from django.http import HttpResponse
from django.urls import reverse
from django.views import View
from django.shortcuts import redirect


def home(request):
    return HttpResponse("Welcome to Home Page")


def contact(request):
    return HttpResponse("Contact View - Function Based View")




def profile(request, username):
    return HttpResponse(f"Welcome to {username}'s profile")


def product(request, id):
    # Redirects to the blog URL
    return redirect('blog', id)


def blog(request, slug):
    return HttpResponse(f"Welcome to blog: {slug}")


def item_detail(request, item_id):
    return HttpResponse(f"Welcome to item {item_id}")


def media_handler(request, path):
    return HttpResponse(f"Serving media file: {path}")


def go_to_post(request):
    url=reverse('go_to_post')
    return HttpResponse(f'url path:{url}')
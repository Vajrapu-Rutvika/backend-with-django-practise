from django.http import HttpResponse
from django.views import View
def home(request):
    return HttpResponse("welcome to home page")
def contact(request):
    return HttpResponse("content view function based on function")
class about(View):
    def get(self,request):
        return HttpResponse("class based view")
def profile(request,username):
    return HttpResponse(f"welcome to {username}'s profile")
def product(request,id):
    return HttpResponse(f"welcome to product {id}")
def blog(request,slug):
    return HttpResponse(f"welcome to blog {slug}")
def item_detail(request,item_id):
    return HttpResponse(f"welcome to item {item_id}")
def media_handler(request, path):
    # Handle media files here
    return HttpResponse(f"Serving media file: {path}")
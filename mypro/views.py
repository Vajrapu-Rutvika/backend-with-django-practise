from django.http import HttpResponse
from django.views import View

def home(request):
    return HttpResponse("welcome to home page")
def contact(request):
    return HttpResponse("content view function based on function")
class about(View):
    def get(self,request):
        return HttpResponse("class based view")
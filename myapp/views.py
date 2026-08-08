from django.shortcuts import render


# def home(request):
#     context={
#         'user_name': 'Rutvika',
#         'items': ['mobile', 'laptop', 'tv'],
#         "name": "Rutvika",
#         "is_logged_in": False,
#     }
#     return render(request,'home.html', context)
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
from datetime import datetime

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
def post_detail(request):
    post={
        'title': 'My first post',
        'created_at':datetime(2025,1,24,10,22),
    }
    return render(request,'post_detail.html', {'post': post})
def profile(request):
    user={
        'username': 'Rutvika',
    }
    return render(request,'profile.html', {'user': user})
def users(request):
    users=["rutvika","malathi","suresh"]
    return render(request,'users.html', {'users': users})

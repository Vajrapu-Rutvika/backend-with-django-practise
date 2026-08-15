from datetime import datetime
from .models import BlogPost, Profile, blog ,Comments,student,Courses
from django.shortcuts import render
from django.contrib.auth.models import User



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
def product_detail(request):
    product={"name":"mobile","price":10000}
    return render(request,'product_detail.html', {'product': product})
def welcome(request):
    user={"is_authenticated": False, "username": "Rutvika"}
    return render(request,'welcome.html', {'user': user})
def items_list(request):
    items=["item1","item2","item3"]
    return render(request,'item.html', {'items': items})
def posts_list(request):
    posts=BlogPost.objects.all()
    return render(request,'post_list.html', {'posts': posts})
def one_to_one_demo(request):
    users=User.objects.select_related('profile').all()
   # profile=Profile.objects.filter(user=user).first()
    return render(request,'one_to_one.html', {'users': users})
def one_to_many_demo(request):
    blogs=blog.objects.prefetch_related('comment_set').all()
    return render(request,'one_to_many.html', {'blogs': blogs,'comment': Comments})

def many_to_many_demo(request):
    students = student.objects.all()
    return render(request, 'manytomany.html', {'students': students})
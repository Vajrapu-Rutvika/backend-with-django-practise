from django.contrib import admin
from .models import BlogPost, Profile, blog,Comments, student,Courses
# Register your models here.
admin.site.register(BlogPost)
admin.site.register(Profile)
admin.site.register(blog)
admin.site.register(Comments)
admin.site.register(student)
admin.site.register(Courses)
from django.contrib import admin
from .models import Author, BlogPermissionPost, BlogPost, Book, Profile, blog,Comments, student,Courses,Author
# Register your models here.
admin.site.register(BlogPost)
admin.site.register(Profile)
admin.site.register(blog)
admin.site.register(Comments)
admin.site.register(student)
admin.site.register(Courses)
admin.site.register(BlogPermissionPost)
admin.site.register(Author)
admin.site.register(Book)


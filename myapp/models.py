from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    views=models.IntegerField(default=0)
    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE) 
    bio=models.TextField()
    location=models.CharField(max_length=100)   

class blog(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
class Comments(models.Model):
    blog=models.ForeignKey(blog, on_delete=models.CASCADE) 
    text=models.TextField()
class Courses(models.Model):
    name=models.CharField(max_length=100)    

class  student(models.Model):
    name=models.CharField(max_length=100)
    courses=models.ManyToManyField(Courses)   



class BlogPermissionPost(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# Backward-compatibility alias for older imports
blogpermissionpost = BlogPermissionPost

class Author(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title=models.CharField(max_length=200)
    author=models.ForeignKey(Author, on_delete=models.CASCADE)
    price=models.DecimalField(max_digits=6, decimal_places=2)
    published_date=models.DateField()

    def __str__(self):
        return self.title
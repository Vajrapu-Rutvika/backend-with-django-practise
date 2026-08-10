from django.db import models

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
from django import forms

from myapp.models import BlogPost

# class contactform(forms.Form):
#     name = forms.CharField(max_length=100)
#     email = forms.EmailField(required=True)
#     message = forms.CharField(widget=forms.Textarea)

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'published']    
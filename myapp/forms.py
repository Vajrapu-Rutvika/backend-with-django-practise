from django import forms
from django.contrib.auth.models import User

from myapp.models import BlogPost

# class contactform(forms.Form):
#     name = forms.CharField(max_length=100)
#     email = forms.EmailField(required=True)
#     message = forms.CharField(widget=forms.Textarea)



class registrationform(forms.Form):
    username = forms.CharField(max_length=20,required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput,required=True)
    confirm_password=forms.CharField(widget=forms.PasswordInput,required=True)

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already registered.")
        return username

    def clean_email(self):
        email=self.cleaned_data.get('email')
        if not email.endswith('@example.com'):
            raise forms.ValidationError("Please use a valid example.com email address.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'published']   

class eventform(forms.Form):
    name=forms.CharField(max_length=100)
    date=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    time=forms.TimeField(widget=forms.TimeInput(attrs={'type':'time'}))
    location=forms.CharField(max_length=200)
    description=forms.CharField(widget=forms.Textarea)         
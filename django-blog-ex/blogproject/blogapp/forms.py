from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:         # Blog 클래스에 대한 이름표 역할
        model = Blog
        fields = ['title', 'writer', 'body', 'image']

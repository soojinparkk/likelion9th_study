from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    # ModelForm customizing
    title = forms.CharField(
        label="제목:",
        widget=forms.TextInput(attrs={
            "placeholder": "제목을 입력해주세요",
        })
    )
    writer = forms.CharField(
        label="작성자:",
        widget=forms.TextInput(attrs={
            "placeholder": "작성자를 입력해주세요",
        })
    )
    body = forms.CharField(
        label="내용:",
        widget=forms.Textarea(attrs={
            "placeholder": "내용을 입력해주세요",
            'cols': 50, 'rows': 13
        })
    )
    image = forms.ImageField(
        label="",
        widget=forms.FileInput(attrs={
            "placeholder": "작성자를 입력해주세요"
        })
    )

    class Meta:         # Blog 클래스에 대한 이름표 역할
        model = Blog
        fields = ['title', 'writer', 'body', 'image']

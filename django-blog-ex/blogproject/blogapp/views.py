from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone

def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs': blogs})

def detail(request, id):
    # blog = Blog.objects.get(id = id)
    blog = get_object_or_404(Blog, pk = id)
    return render(request, 'detail.html', {'blog': blog})

def new(request):
    return render(request, 'new.html')

def create(request):
    new_blog = Blog()                                   # 새로운 객체에 저장
    new_blog.title = request.POST['title']
    new_blog.write = request.POST['writer']
    new_blog.body = request.POST['body']
    new_blog.pub_date = timezone.now()                  # 현재 시각 저장
    new_blog.save()
    return redirect('detail', new_blog.id)              # detail 호출

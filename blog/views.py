from django.shortcuts import render, get_object_or_404
from blog.models import Post

# Create your views here.


def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})


def post(request, slug):
    posts = Post.objects.all()
    return render(request, 'post.html', {'post': get_object_or_404(Post, slug=slug), 'posts': posts})


def about(request):
    return render(request, 'about.html', {})

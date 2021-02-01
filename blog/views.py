from django.shortcuts import render, get_object_or_404
from .models import BlogPost

# Create your views here.

def all_blogs(request):
    blogs = BlogPost.objects.order_by('-date')
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})

def detail(request, post_id):
    blog = get_object_or_404(BlogPost, pk=post_id)
    return render(request, 'blog/detail.html', {'blog':blog})
from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from .models import Post


def blog(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'pages/blog.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'pages/blog.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(ListView):
    model = Post
    template_name = 'pages/post_detail.html'


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']

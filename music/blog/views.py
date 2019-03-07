from django.shortcuts import render
from . import models


def blog_view(request):
    posts = models.blog.objects.all()
    context_blog = {
        'blog_posts': posts
    }
    return render(request, 'pages/blog.html', context=context_blog)

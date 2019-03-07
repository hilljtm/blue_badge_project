from django.shortcuts import render, HttpResponse
from .models import Post


def blog(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'pages/blog.html', context)

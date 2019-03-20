
from django.shortcuts import render, HttpResponse
from .models import Indiv_vid
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView


def Indiv_vid_view(request):
    comment = Indiv_vid.objects.all()

    context = {
        'comments': comment
    }

    return render(request, 'pages/indiv_vid.html', context)

from django.shortcuts import render
from .models import Indiv_vid


def Indiv_vid_view(request):
    context = {
        'comments': Indiv_vid.object.all()
    }
    return render(request, 'pages/indiv_vid.html', context)

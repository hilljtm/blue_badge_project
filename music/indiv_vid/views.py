
from django.shortcuts import render, HttpResponse
from .models import Indiv_vid
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView
from main.models import our_picks


def Indiv_vid_view(request):
    comment = Indiv_vid.objects.all()
    top_picks = our_picks.objects.all()

    context = {
        'comments': comment,
        'picks': top_picks
    }

    return render(request, 'pages/indiv_vid.html', context)


class newComment(LoginRequiredMixin, CreateView):
    model = Indiv_vid
    fields = ['content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

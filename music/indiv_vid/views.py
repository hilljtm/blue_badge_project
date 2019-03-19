
from django.shortcuts import render
from .models import Indiv_vid
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView


def Indiv_vid_view(request):
    comment = Indiv_vid.objects.all()

    context = {
        'comments': comment
    }

    return render(request, 'pages/indiv_vid.html', context)


class PostCreateView(LoginRequiredMixin):
    model = Indiv_vid
    # fields = ['content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

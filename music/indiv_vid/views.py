
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


class PostListView(ListView):
    model = Indiv_vid
    template_name = 'pages/blog.html'
    context_object_name = 'comments'
    ordering = ['-date_posted']


class PostCreateCommentView(LoginRequiredMixin, CreateView):
    model = Indiv_vid
    fields = ['content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

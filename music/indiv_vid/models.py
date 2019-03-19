
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from main.models import our_picks


class Indiv_vid(models.Model):
    filter_by = our_picks.embed
    content = models.CharField(max_length=300)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse('indiv_vid')

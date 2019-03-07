from django.db import models
from django.contrib.auth.models import User
import datetime


class our_picks(models.Model):
    song_title = models.CharField('Title', max_length=30)
    link = models.CharField('link', max_length=500)

    def __str__(self):
        return self.song_title

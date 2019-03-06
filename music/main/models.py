from django.db import models
import django_tables2 as tables


class our_picks(models.Model):
    song_title = models.CharField('Title', max_length=30)
    link = models.CharField('link', max_length=500)

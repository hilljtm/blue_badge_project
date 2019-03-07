from main.models import *
from django.contrib.auth.models import User


class blog(models.Model):
    User = User
    blog_post = models.CharField('Post:', max_length=500)
    date = datetime.datetime.now()

    def __str__(self):
        return self.blog_post

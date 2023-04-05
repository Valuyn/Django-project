from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Tag(models.Model):
    title = models.CharField(max_length=15)
    description = models.Charfield(max_length=150)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag-detail', kwargs={'pk': self.pk})


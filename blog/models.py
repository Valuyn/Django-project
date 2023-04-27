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
    description = models.CharField(max_length=100, default="now empty")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tag-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    body = models.TextField()
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'comment by {self.name} on {self.post}'

    def get_absolute_url(self):
        return reverse('comment-create', kwargs={'pk': self.pk})

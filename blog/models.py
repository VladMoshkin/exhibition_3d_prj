from django.db import models
from django.utils import timezone


class Post(models.Model):
    preview = models.ImageField(upload_to='blog_preview', null=True, blank=True)
    background = models.ImageField(upload_to='blog_background', null=True, blank=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

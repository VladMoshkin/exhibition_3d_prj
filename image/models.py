from django.db import models
from django.utils import timezone


class Image(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    exhibition = models.ForeignKey('exhibition.Exhibition', on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images', null=True)
    created_date = models.DateTimeField(default=timezone.now)
    approved = models.BooleanField()

    def __str__(self):
        return self.title

from django.db import models
from django.utils import timezone


class Exhibition(models.Model):
    preview_right = models.ImageField(upload_to='exhibition_preview', null=True, blank=True)
    preview_left = models.ImageField(upload_to='exhibition_preview', null=True, blank=True)
    preview_top = models.ImageField(upload_to='exhibition_preview', null=True, blank=True)
    preview_bottom = models.ImageField(upload_to='exhibition_preview', null=True, blank=True)
    preview_front = models.ImageField(upload_to='exhibition_preview', null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateTimeField(
            default=timezone.now)
    open_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

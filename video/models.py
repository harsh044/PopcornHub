from unicodedata import category
from django.db import models


# Create your models here.
class Video(models.Model):
    file_path = models.CharField(max_length=255, blank=True, null=True)

    video_src = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=100,blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    duration = models.CharField(max_length=255,blank=True, null=True)
    thumbnail = models.CharField(max_length=255, blank=True, null=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    category = models.CharField(max_length=255, blank=True, null=True)
    resolution = models.CharField(max_length=255, blank=True, null=True)
    language = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.title

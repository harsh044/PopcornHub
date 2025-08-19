# import post_save
from django.db.models.signals import post_save
from django.dispatch import receiver

from video.models import Video
# from pytube import YouTube
import yt_dlp

@receiver(post_save, sender=Video)
def video_post_save(sender, instance, created, **kwargs):
    if created:
        video_path = instance.file_path
        get_video_id = video_path.split(".be/")[1]
        
        ydl_opts = {}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_path, download=False)
            
        instance.video_src = f"https://www.youtube.com/embed/{get_video_id}?rel=0"
        instance.title = info.get("title")
        instance.description = info.get("description")
        instance.duration = info.get("duration_string")
        instance.thumbnail = info.get("thumbnail")
        instance.views = info.get("view_count")
        instance.likes = info.get("like_count")
        instance.resolution = info.get("resolution")
        instance.language = "Marathi" if info.get("language") == "mr" else 'Hindi'
        instance.category = info.get("categories")[0]

        instance.save()
        print(f"Video created: {instance.title}")
    else: 
        # Logic to execute after a Video instance is updated
        print(f"Video updated: {instance.title}")

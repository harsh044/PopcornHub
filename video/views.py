from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

from video.models import Video


# Create your views here.
def video_list(request):
    """View to list all videos."""
    videos = Video.objects.all()
    return render(request, "video/video_list.html", {"videos": videos})


def video_detail(request, video_id):
    """View to display a single video."""
    video = Video.objects.get(id=video_id)
    # hls_url = reverse("serve_hls_playlist", args=[video_id])
    related_movies = Video.objects.filter(category=video.category)
    return render(request, "video/video_player.html", {"video": video,"related_movies":related_movies})

def trending_videos(request):
    videos = Video.objects.all().order_by('-views')
    return render(request, "video/trending_videos.html", {"videos": videos})

def category_movie(request):
    """View to display a single video."""
    video = list(Video.objects.values_list('category', flat=True).distinct())
    return render(request, "video/category.html", {"videos": video})

def selected_category(request, category):
    movies = Video.objects.filter(category=category)
    
    return render(request, "video/selected_category.html", {"movies":movies})
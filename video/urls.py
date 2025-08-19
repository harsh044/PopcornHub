from django.urls import path

from video.views import video_detail, video_list,trending_videos,category_movie,selected_category

urlpatterns = [
    path("", video_list, name="video_list"),
    path("trending_videos", trending_videos, name="trending_movies"),
    path("category", category_movie, name="category_movie"),
    path("selected_category/<str:category>/", selected_category, name="selected_category"),
    path("<int:video_id>/", video_detail, name="video_detail"),
]

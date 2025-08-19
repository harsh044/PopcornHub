from django.contrib import admin

from video.models import Video


# Register your models here.
@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ("title", "uploaded_at", "duration")
    search_fields = ("title", "description")
    list_filter = ("uploaded_at",)
    ordering = ("-uploaded_at",)

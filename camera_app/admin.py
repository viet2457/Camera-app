from django.contrib import admin
from .models import CameraConfig

@admin.register(CameraConfig)
class CameraConfigAdmin(admin.ModelAdmin):
    list_display = ('name', 'camera_type', 'video_path', 'created_at')
    list_filter = ('camera_type',)
    search_fields = ('name', 'video_path')
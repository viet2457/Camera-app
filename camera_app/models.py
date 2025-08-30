from django.db import models

class CameraConfig(models.Model):
    CAMERA_TYPES = (
        ('basler', 'Basler'),
        ('video', 'Video'),
    )
    name = models.CharField(max_length=100, unique=True)
    camera_type = models.CharField(max_length=20, choices=CAMERA_TYPES)
    video_path = models.CharField(max_length=255, blank=True, null=True, help_text='Required for video camera type')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.camera_type})"
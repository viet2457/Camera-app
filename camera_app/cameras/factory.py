from .base import Camera
from .basler import BaslerCamera
from .video import VideoCamera
import queue

class CameraFactory:
    @staticmethod
    def create_camera(camera_type: str, buffer: queue.Queue, **kwargs) -> Camera:
        if camera_type.lower() == "basler":
            return BaslerCamera(buffer)
        elif camera_type.lower() == "video":
            video_path = kwargs.get("video_path")
            if not video_path:
                raise ValueError("video_path is required for VideoCamera")
            return VideoCamera(buffer, video_path)
        else:
            raise ValueError(f"Unknown camera type: {camera_type}")
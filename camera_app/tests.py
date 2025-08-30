from django.test import TestCase
from .models import CameraConfig
from .cameras.factory import CameraFactory
import queue

class CameraTests(TestCase):
    def test_camera_config_creation(self):
        config = CameraConfig.objects.create(
            name="Test Camera",
            camera_type="video",
            video_path="/path/to/test.mp4"
        )
        self.assertEqual(config.name, "Test Camera")
        self.assertEqual(config.camera_type, "video")
        self.assertEqual(config.video_path, "/path/to/test.mp4")

    def test_camera_factory_basler(self):
        buffer = queue.Queue(maxsize=10)
        camera = CameraFactory.create_camera("basler", buffer)
        self.assertEqual(camera.__class__.__name__, "BaslerCamera")

    def test_camera_factory_video(self):
        buffer = queue.Queue(maxsize=10)
        camera = CameraFactory.create_camera("video", buffer, video_path="test.mp4")
        self.assertEqual(camera.__class__.__name__, "VideoCamera")

    def test_camera_factory_invalid_type(self):
        buffer = queue.Queue(maxsize=10)
        with self.assertRaises(ValueError):
            CameraFactory.create_camera("invalid", buffer)
from .base import Camera
import cv2
import queue

class VideoCamera(Camera):
    def __init__(self, buffer: queue.Queue, video_path: str):
        super().__init__(buffer)
        self.cap = cv2.VideoCapture(video_path)
        if not self.cap.isOpened():
            raise ValueError(f"Could not open video file: {video_path}")

    def capture_frames(self):
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                self.buffer.put(frame)
            else:
                break
        self.cap.release()
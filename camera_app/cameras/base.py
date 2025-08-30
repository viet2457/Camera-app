from abc import ABC, abstractmethod
import queue

class Camera(ABC):
    def __init__(self, buffer: queue.Queue):
        self.buffer = buffer

    @abstractmethod
    def capture_frames(self):
        """Capture frames and put them into the buffer."""
        pass
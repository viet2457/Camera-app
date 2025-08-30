from .base import Camera
from pypylon import pylon

class BaslerCamera(Camera):
    def __init__(self, buffer: queue.Queue):
        super().__init__(buffer)
        # Initialize Basler camera 
        self.camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateFirstDevice())
        self.camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)

    def capture_frames(self):
        while True:  # Continuous capture; stop via external signal in production
            grab_result = self.camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
            if grab_result.GrabSucceeded():
                frame = grab_result.Array 
                self.buffer.put(frame)
            grab_result.Release()
       
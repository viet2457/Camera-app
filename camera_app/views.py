import queue
import threading
from django.http import JsonResponse
from django.views import View
from .cameras.factory import CameraFactory
from .models import CameraConfig

class CameraView(View):
    def get(self, request):
        buffer = queue.Queue(maxsize=10)  
        camera_id = request.GET.get("camera_id")
        
        try:
            # Fetch camera config from database
            config = CameraConfig.objects.get(id=camera_id)
            camera_type = config.camera_type
            kwargs = {}
            if camera_type == "video":
                if not config.video_path:
                    return JsonResponse({"error": "Video path is required for video camera"}, status=400)
                kwargs["video_path"] = config.video_path

            
            camera = CameraFactory.create_camera(camera_type, buffer, **kwargs)
            
            
            thread = threading.Thread(target=camera.capture_frames, daemon=True)
            thread.start()

            return JsonResponse({
                "status": "Camera started",
                "camera_id": config.id,
                "type": camera_type
            })
        except CameraConfig.DoesNotExist:
            return JsonResponse({"error": "Camera config not found"}, status=404)
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=400)

# In urls.py, add: path('camera/start/', CameraView.as_view(), name='camera_start')
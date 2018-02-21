import cv2
from base_camera import BaseCamera

class Camera(BaseCamera):
    video_source = 0

    @staticmethod
    def set_video_source(source):
        Camera.video_source = source
    
    @staticmethod
    def frames():
        camera = cv2.VideoCapture(Camera.video_source)
        if not camera.isOpened():
            raise RuntimeError('could not start camera')

        while True:
            _, img = camera.read()

            yield cv2.imencode('.jpg', img)[1].tobytes()
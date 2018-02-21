from flask import Flask, render_template, Response
from importlib import import_module
import os

if os.environ.get('CAMERA'):
    Camera = import_module('camera_' + os.environ['CAMERA']).Camera
else:
    from camera import Camera

app = Flask(__name__)

"""credit to miguel grinberg"""

@app.route('/')
def index():
    return render_template('base.html')

def gen(Camera):
    """Video Streaming generator function"""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    """video streaming route. put this in the src attribute of an img tag"""
    return Response(gen(Camera()), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', threaded=True)


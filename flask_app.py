from flask import Flask, render_template, Response,redirect
from importlib import import_module
import os
from camera_pi import Camera

app = Flask(__name__)

"""credit to miguel grinberg"""

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    """Video Streaming generator function"""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    """video streaming route. put this in the src attribute of an img tag"""
    return Response(gen(Camera()), mimetype='multipart/x-mixed-replace; boundary=frame')


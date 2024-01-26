from picamera2 import Picamera2
import cv2
from flask import Flask, Response


#Argparse
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--width", type=int, default=1280, nargs="?", action="store",
                    help="live video capture width")
parser.add_argument("--height", type=int, default=720, nargs="?", action="store",
                    help="live video capture height")
args = parser.parse_args()


app = Flask(__name__)

def generate_frames():
    picam2 = Picamera2()
    picam2.preview_configuration.main.size = (args.width,args.height)
    picam2.preview_configuration.main.format = "RGB888"
    picam2.preview_configuration.align()
    picam2.configure("preview")
    picam2.start()

    while True:
        im = picam2.capture_array()
        if not im.any():
            break
        
        rotated = cv2.rotate(im, cv2.ROTATE_180)

        _, buffer = cv2.imencode('.jpg', rotated)
        frame_bytes = buffer.tobytes()

        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
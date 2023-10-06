from django.shortcuts import render

# Create your views here.

import cv2
from django.http import StreamingHttpResponse
from django.views.decorators import gzip

def home(request):
    return render(request,'home.html')


def test(request):
    return render(request,'video_stream.html')


@gzip.gzip_page
def video_feed(request):
    cap = cv2.VideoCapture(0)  # Open the default camera (change index as needed)

    def generate():
        while True:
            ret, frame = cap.read()
            frame=cv2.flip(frame,1)
            if not ret:
                break

            # Process your frame here if needed

            # Encode the frame as JPEG
            _, buffer = cv2.imencode('.jpg', frame)
            frame_bytes = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

    return StreamingHttpResponse(generate(), content_type='multipart/x-mixed-replace; boundary=frame')

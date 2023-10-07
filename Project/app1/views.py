from django.shortcuts import render

# Create your views here.
#import for project-image processing
import cv2
from ultralytics import YOLO
import cvzone
import math
from django.contrib.auth.hashers import make_password,check_password
from django.http import StreamingHttpResponse
from django.views.decorators import gzip
from app1.models import Authenticator
model=YOLO('model/model-2.pt')

# pbkdf2_sha256$600000$YzaRneKQIHyrkEyoPN70H0$VEw7JwjlrY/c7QZuM08lgK3Jm9gB04gcF25wx/Kfv8A=

def login(request):
    context={
        'message':'yes'
    }
    return render(request,'login2.html')

def login_validation(request):
    print("we are at login oage")
    context={
        'message':"wrong id-pass"
    }
    if(request.method=='POST'):
        username=request.POST.get('username')
        pwd=request.POST.get('password')
        print(username,pwd)
        a=Authenticator.objects.all()[0].username
        b=Authenticator.objects.all()[0].password
        if a==username and b==pwd:
            return render(request,'video_stream.html')
        else:
            return render(request,'login2.html',context)

    return render(request,'home.html')

def home(request):
    print(make_password('viit123'))
    return render(request,'home.html')


def test(request):
    return render(request,'video_stream.html')


@gzip.gzip_page
def video_feed(request):
    cap = cv2.VideoCapture('static/video/vid-3.mp4')  # Open the default camera (change index as needed)
    def generate():
        while True:
            ret, frame = cap.read()
            # frame=cv2.flip(frame,1)
            if not ret:
                break

            # Process your frame here if needed
            fireResult=model(frame,stream=True)
            for r in fireResult:
                for box in r.boxes:
                    x1,y1,x2,y2=box.xyxy[0]
                    x1,y1,x2,y2=int(x1),int(y1),int(x2),int(y2)
                    conf=math.ceil(box.conf[0]*100)/100
                    w,h=x2-x1,y2-y1
                    cvzone.cornerRect(frame,(x1,y1,w,h),l=9,rt=2,colorC=(0,255,0))
                    cvzone.putTextRect(frame,f'fire : {conf}',(max(0, x1), max(35, y1)),scale=1,thickness=1, offset=10)
            # Encode the frame as JPEG
            _, buffer = cv2.imencode('.jpg', frame)
            frame_bytes = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

    return StreamingHttpResponse(generate(), content_type='multipart/x-mixed-replace; boundary=frame')

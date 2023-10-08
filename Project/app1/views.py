from django.shortcuts import render,redirect
from twilio.rest import Client
import random
# Create your views here.
#import for project-image processing
import cv2
from ultralytics import YOLO
import cvzone
import math
from django.contrib.auth.hashers import make_password,check_password
from django.http import StreamingHttpResponse
from django.views.decorators import gzip
from app1.models import Authenticator,Contact
from app1.models import Concern
from .forms import ImageForm

model=YOLO('model/model-2.pt')


# pbkdf2_sha256$600000$YzaRneKQIHyrkEyoPN70H0$VEw7JwjlrY/c7QZuM08lgK3Jm9gB04gcF25wx/Kfv8A=

def raiseConcern(request):
    print('we are here')
    if(request.method =='POST'):
        print('we are here tooo')
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            print('form is valid')
            form.save()
            obj=form.instance
            return redirect(request,'home.html')
    print('yess i got here')
    form = ImageForm()
    con=Concern.objects.all()
    return render(request, 'home.html', {'data':con,'form': form})
    

# def image_list(request):
#     images = ImageWithCharField.objects.all()
#     return render(request, 'image_list.html', {'images': images})


def otpExecutor(entry):
    print('sms sent')
    for person in entry:
        number=person.number
        if str(number)=='8579088702':
            otp=random.randint(1000,9999)

            auth_sid="AC09d19866493ee5092d3203d4b88a69f4"
    #
            auth_token="06faa0bde6f8c8cbac5d2e683d2ca4e0"
    #
            number='+91'+str(number)
            client=Client(auth_sid,auth_token)
            message=client.messages.create(
            body=f"Alert!!! Fire has been Detected in your region {entry[0].location}.Please exercise necessary precautions and wait for our help!!!",
            from_="+17169514074",
            to='+919158158170'
            )
    return 1

def register_validation(request):
    if(request.method=='POST'):
        name=request.POST.get('name')
        number=request.POST.get('number')
        location=request.POST.get('location')
    if len(number)==10:
        cont=Contact(name=name,number=number,location=location)
        cont.save()
        context={
            'success':'yes'
        }
        return render(request,'home.html')
    else:
        context={
            'error':"yes"
        }
        return render(request,'addNumber2.html',context)
    
    return render(request,'addNumber2.html')

def addNumber(request):
    return render(request,'addNumber2.html')

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
            con=Concern.objects.all()
            return render(request,'admin.html',{'con':con})
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
    cap = cv2.VideoCapture('static/video/vid5.mp4')  # Open the default camera (change index as needed)
    def generate():
        fireDetected=0
        firePercentage=0

        while True:
            ret, frame = cap.read()
            # frame=cv2.flip(frame,1)
            if not ret:
                break
            # Process your frame here if needed
            fireResult=model(frame,stream=True)
            sh,sw,c=frame.shape
            ta=sh*sw*0.5
            if fireResult:
                if fireDetected==0 and firePercentage>30:
                    entry=Contact.objects.all()
                    # fireDetected=otpExecutor(entry)

            for r in fireResult:
                fireArea=0
                for box in r.boxes:
                    x1,y1,x2,y2=box.xyxy[0]
                    x1,y1,x2,y2=int(x1),int(y1),int(x2),int(y2)
                    conf=math.ceil(box.conf[0]*100)/100
                    w,h=x2-x1,y2-y1
                    currentArea=int(0.5*h*w)
                    fireArea=fireArea+currentArea
                    cvzone.cornerRect(frame,(x1,y1,w,h),l=9,rt=2,colorC=(0,255,0))
                    cvzone.putTextRect(frame,f'fire : {conf}',(max(0, x1), max(35, y1)),scale=1,thickness=1, offset=10)
            # Encode the frame as JPEG
                # cv2.putText(img,f'{int(conf)}',(x1,y1-20),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,0),1)
                firePercentage=int((fireArea/ta)*100)
                cv2.putText(frame,f'Total Area : {firePercentage}%',(10,70),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,0),1)
            _, buffer = cv2.imencode('.jpg', frame)
            frame_bytes = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

    return StreamingHttpResponse(generate(), content_type='multipart/x-mixed-replace; boundary=frame')

from django.shortcuts import render
import qrcode
import time
from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings


class GenerateQrCode(APIView):
    def post(self,request):
        data=request.data
        message=data["message"]
        img=qrcode.make(message)  # to generating qr code 
        AbsoluteUrl=request.build_absolute_uri()   # it return absoluteurl
        img_name = 'qr' + str(time.time()) + '.png'
        hostName=request.get_host()    #'127.0.0.1:8000' like this 
        ImageFullPath=hostName+"/"+"media" +"/"+ img_name      #http://127.0.0.1:8000/media/qr1665397633.338255.png
        img.save(str(settings.MEDIA_ROOT) + '/' + img_name)

        return Response({'img_name': ImageFullPath})


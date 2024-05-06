from django.http import JsonResponse
from django.shortcuts import render
from url.models import User
from url.models import Url
from django.db.models import Q
from random import randint
from django.core.mail import send_mail
import url
from url_shortner import urls

# Create your views here.

##################### create ###########################
def create(request):
    uname=request.POST.get('username')
    mail=request.POST.get('email')
    pwd=request.POST.get('password')
    data=User.objects.filter(Q(email=mail) and Q(user_name=uname))
    if len(data)>0:
        return JsonResponse("this email and username alreay exist",safe=False)
    ot=otp(4)
    send_mail('otp verification',
        'your otp is '+ot,
        'bairwavinod499@gmail.com',
        [mail])
    user=User(user_name=uname,email=mail,password=pwd,otp=ot,is_verified=0)
    user.save()
    return JsonResponse('profile created succesfully',safe=False)

###################### otp ############
def otp(digit):
    otp=[]
    for i in range (digit):
        num=randint(0,9)
        otp.append(str(num))
    return ''.join(otp)    
 
 ########################## verify #############   
def verify(request):
    mail=request.POST.get('email')
    ot=request.POST.get('otp')   
    data=User.objects.get(email=mail)
    if data.otp==ot:
        data.is_verified=1
        data.save()
        return JsonResponse('your account has been successfully verified',safe=False)
    return JsonResponse("your otp is invalid",safe=False)

###################### login ############
def login(request):
    mail=request.POST.get('email')
    pwd=request.POST.get('password')
    try:  
        data=User.objects.get(email=mail,password=pwd)
        if data.is_verified==1:
           return JsonResponse("login successfully",safe=False)
        else:
            return JsonResponse("your account is not verified",safe=False)

    except url.models.User.DoesNotExist:
        return JsonResponse("password or email incorrect",safe=False)

############# forget password ##########

def forgot_password(request):
    uname=request.GET.get("username")
    try:
        data=User.objects.get('user_name=uname')
        pwd=otp(8)
        send_mail('new password',
                'your password is '+pwd,
                'bairwavinod499@gmail.com',
                [data.email])
        data.password=pwd
        data.save()       
    except url.models.User.DoesNotExist:
        return JsonResponse("username is not valid",safe=False)
    return JsonResponse("your new password is sent to the mail",safe=False)
    
############## change_password ######    
def change_password(request):
    uname=request.POST.get('username')
    pwd=request.POST.get('oldpassword')
    npwd=request.POST.get('newpassword')
    try:
        data=User.objects.get(user_name=uname,password=pwd)
        data.password=npwd
        data.save()
    except url.models.User.DoesNotExist:
        return JsonResponse("either username or old password is in valid",safe=False)
    return JsonResponse("password has been change successfully",safe=False)

############## url shortner #############  class url ####
def url_shortner(request):
    long=request.POST.get('longurl')
    short=request.POST.get('shorturl')
    uid=request.POST.get('userid')
    data=Url.objects.filter(short_url=short)
    if len(data)>0:
        return JsonResponse("that custom hash is already in used",safe=False)
    if uid==None:
        uid=0
    url=Url(long_url=long,short_url=short,user_id=uid)
    url.save()
    return JsonResponse("short url successfully created",safe=False)

############ long url###########
def get_long_url(request):
    short=request.GET.get('shorturl')
    try:
        data=Url.objects.get(short_url='cpt.cc/csd'+ short)
        result={data.short_url:data.long_url}
        return JsonResponse(result)
    except url.models.Url.DoesNotExist:
        return JsonResponse("this short url is not link with any url ",safe=False)
    
#     ############ all url###########
def get_all_url(request):
    uid=request.GET.get('userid')
    data=urls.objects.filter(user_id=uid)
    result={}
    for obj in data:
        result[obj.short_url]=obj.long_url
    return JsonResponse(result)    
        
            
    
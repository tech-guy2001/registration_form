from django.shortcuts import render
from login_app.models import deatils
from django.core.mail import send_mail
from django.conf import settings
import random


# Create your views here.

def sgin_up(request):
    if request.method=="POST":
        fname=request.POST.get('first')
        lname=request.POST.get('last')
        email=request.POST.get('email')
        password=request.POST.get('password')
        if deatils.objects.filter(first_name=email).exists():
            return render(request,'sign.html',{"name":"Email already exists"})
        else:
            if deatils.objects.filter(email=email).exists():
                return render(request,'sign.html',{"name":"Email already exists"})
            else:
                deatils.objects.create(first_name=fname,last_name=lname,email=email,password=password)
                d={"name":fname+" "+lname+"is successfully added"}
                send_mail('thank you for regtration  your login details',f"user:{fname} and your password {password}",'settings.EMAIL_HOST_USER',[email],fail_silently=False)
                return render(request,'sign.html',d)

    return render(request,'sign.html')

def sgin_in(request):
     if request.method=="POST":
        fname=request.POST.get('first')
        passwords=request.POST.get('password')
        search=deatils.objects.get(first_name=fname)
        if search.password==passwords:
            return render(request,'main.html')
        else:
            return render(request,'sign.html',{"name":"enter login details is worng"})
def forget(request):
    if request.method=="POST":
        global email,d
        email=request.POST.get('email')
        random_number = random.randint(1000, 9999)
        d={}

        d[email]=random_number
        print(d)
          
        
        if deatils.objects.filter(email=email).exists():
            send_mail('one time password',f'{random_number}','settings.EMAIL_HOST_USER',[email],fail_silently=False)
            return render(request,'forget.html',{"name":"otp is sent to your email"})
        
        else:
            return render(request,'forget.html',{"name":"your email not regster"})
    return render(request,'forget.html')
def otp(request):
    if request.method=="POST":
        otp=request.POST.get('otp')
        print(type(d[email]))
        print(d[email])
        if email in d:
            if d[email]==int(otp):
                return render(request,'change.html')
            else:
                return render(request,'forget.html',{"name":f'otp is invalid"{otp}'})
        else:
            return render(request,'forget.html',{"name":f'email  is invalid"{otp}'})
def password(request):
    if request.method=="POST":
        np=request.POST.get("npassword")
        cp=request.POST.get("cpassword")
        if np==cp:
            deatils.objects.filter(email=email).update(password=np)
            return render(request,'change.html',{"name":f'your password is changed'})
        
        
        else:
            return render(request,'change.html',{"name":f'invaild password'})
        
        



        





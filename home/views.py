from multiprocessing import context
from django.shortcuts import redirect, render, HttpResponse

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from datetime import datetime

from numpy import imag
from home.models import Contact ,Event
from home.models import Register
from django.contrib import messages

from .models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("this is homepage")

def about(request):
    return render(request, 'about.html') 

def logout(request):
    return render(request, 'login.html')

def services(request):
    return render(request, 'services.html')

def profile(request):
    return render(request, 'profile.html') 

def forms(request):
    return render(request, 'forms.html') 

def register(request):
    #print(request.method)
    if request.method == "POST":
        
        name1 = request.POST['name1']
        username = request.POST['username']
       # print[email]
        
        password = request.POST['password']
        #printpassword)

        password2 = request.POST['password2']
        if password == password2 :
            if User.objects.filter(username = username).exists():
                messages.info(request,'Email already exist')
                return redirect('/register')
            else :
                user = User.objects.create_user(username,username,password)
                user.save()
                messages.info(request,'Registered Succesfully')
                return redirect('/login')
        # return redirect('/login')
        # messages.success(request, 'You have registered succesfully.'
        else:
            messages.info(request,'Incorrect Password')
            return redirect('/profile')
    else:
        return render(request, 'register.html') 
    

    # return render(request, 'register.html',{'form':form})
 
def login(request):
    if request.method == "POST":
        loginemail = request.POST['loginemail']
        loginpassword = request.POST['loginpassword']
        print(loginemail)
        print(loginpassword) 
        user = authenticate(username = loginemail,password = loginpassword)
        print(user)
        if user is not None:
            #print(2)
            messages.info(request,'Succesfully logged in')
           # login(request,user)
            return redirect ('/forms')
        else:
           # print(1)
            messages.info(request,'Invalid Login')
            return redirect('/login')
    else:
        return render(request,'login.html')
   # return render(request, 'login.html')

def contact(request):
    print(request.method)
    if request.method == "POST":
        print(1)
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')

def events(request):
    if request.method == "POST":
        collegename = request.POST.get('collegename')
        eventname = request.POST.get('eventname')
        date = request.POST.get('date')
        desc = request.POST.get('desc')
        image = request.FILES['image']
        eventdetail = Event(collegename = collegename,eventname = eventname,date = date,desc = desc,image = image)
        eventdetail.save()
        messages.success(request, 'Event detail saved !!')
        return redirect('/forms')
    else:
        return render(request,'events.html')

def allevents(request):
    events=Event.objects.all()
    context={"events":events}
    return render(request,'allevents.html',context)
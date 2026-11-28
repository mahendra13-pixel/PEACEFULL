from django.shortcuts import render,redirect
from.models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate ,login, logout
from django.contrib.auth.decorators import login_required
import re


# Create your views here.
def register(request):
    if request.method == 'POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        password1=request.POST['password1']
        if password == password1:
            error=[]
            if User.objects.filter(username=username).exists():
                error.append("username already exists")
                
            if User.objects.filter(email=email).exists():
                error.append("email already exists")
            
            if not re.search(r'[A-Z]',password):
                error.append('your password must contain atleast one UPPERCASE')
                
            if not re.search(r'\d',password):
                error.append('your password must contain atleast one digit')
            
            if not re.search(r'\W',password):
                error.append('your password must contain atleast one word character')
    
            try:
                validate_password(password)
                
                if not error:
                    User.objects.create_user(first_name=fname,last_name=lname,email=email,username=username,password=password)
                    messages.success(request,"your account is sucessfully registered!!!")
                    return redirect('register')
                
                else:
                    for i in error:
                        messages.error(request,i)
            except ValidationError as e:
                for error in e.messages:
                    messages.error(request,error)
                return redirect('register')    
            
        else:
            messages.error(request,'password doesnt match')
            return redirect('register')
    return render(request,'account/register.html')


def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')
        
        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Username not registered yet!!')
            return redirect('log_in')
    
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
        
        if remember_me:
            print("session")
            request.session.set_expiry(12222)
        else:
            request.session.set_expiry(0) 
    
        next=request.POST.get('next','')
        return redirect(next if next else 'index') 
    else:
        messages.error(request,'Password doesnot match with username')
        return redirect('log_in')   
    next=request.GET.get('next','')
    return render(request, 'account/login.html', {'next': next})

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from appname.models import *
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from .models import *
import datetime
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.models import User, auth
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives

import os
from django.template.loader import render_to_string, get_template
import uuid,random
from django.core.mail import send_mail
from django.shortcuts import render, redirect, HttpResponse,HttpResponseRedirect
from django.http import HttpResponseRedirect
from django.conf import settings
from django.http import JsonResponse
User = get_user_model()

# Create your views here.
def home(request):
    return render(request, 'index.html')

def nots(request):
    return render(request, 'index.html')

def user_login(request):
    if request.user.is_authenticated:
        return redirect('/success/')
    else:
        if request.method == "POST":
            email = request.POST.get("email")
            password = request.POST.get("password")
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                msg = f'Login Success... {request.user.first_name}'
                messages.success(request, msg)
                return redirect('/success/')
            else:
                messages.error(request, 'wrong email and password ....') 
                return render(request, 'index.html')
        return render(request, 'index.html')

def register(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        users = User.objects.create_user(first_name=fname,last_name=lname,email=email,password=password)
        users.save()
        messages.success(request, 'Regiter Success...')
        return redirect('/')
    return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/")

@login_required(login_url='/')
def success(request):
    return render(request, 'success.html')
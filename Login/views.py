
import requests
from django.http import JsonResponse
# Create your views here.
import re
from django.core import mail
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth import authenticate,logout, login as auth_login

from django.contrib.auth.models import User
from .models import Profile
import uuid
from studentportal.settings import *
from django.contrib.auth.decorators import login_required
from sprofile.models import Sprofile
from django.http import JsonResponse
from twilio.rest import Client
import os

def send_message(request):
      
      account_sid = "your account sid"
      auth_token = "your auth token"
      client = Client(account_sid, auth_token)
      message = client.messages.create(
      body="Your Scholarship will be expiry in 28 days",
      from_="your twilio number",
      to="your number"
      )
      print(message.sid)

      return JsonResponse({'success':True})
    



def griffin_s(request):
    return render(request,"Griffiths.html")
def amity_s(request):
    return render(request,"Amitys.html")
def bits_s(request):
    return render(request,"BITSs.html")
def iis_s(request):
    return render(request,"IISBangs.html")
def parul_s(request):
    return render(request,"paruls.html")
def queen_s(request):
    return render(request,"Queenss.html")
def uuic_s(request):
    return render(request,"UIUCs.html")
def auckland_s(request):
    return render(request,"UofAuckland_s.html")
def ottawa_s(request):
    return render(request,"Universityofottawas.html")
def interview(request): 
    return render(request,"interview.html")


def parul(request):
    data = Sprofile.objects.all().filter(user=request.user)[0].current_gpa
    data1 = Sprofile.objects.all().filter(user=request.user)[0].sports
    
    context = {
        'data': data,
        'data1': data1,
        
    }
    return render(request, 'parul.html',context)

def iis(request):
     
     iis_data = Sprofile.objects.all().filter(user=request.user)[0].current_gpa
     context = {
        'iis_data': iis_data,
        
        
    }
     return render(request, 'iis.html',context)
def amity(request):
    amity_data = Sprofile.objects.all().filter(user=request.user)[0].current_gpa
    amity_data1 = Sprofile.objects.all().filter(user=request.user)[0].sports
    
    context = {
        'amity_data': amity_data,
        'amity_data1': amity_data1,
        
    }
    return render(request, 'amity.html',context)

def bits(request):
    bits_data = Sprofile.objects.all().filter(user=request.user)[0].current_gpa
    bits_data1 = Sprofile.objects.all().filter(user=request.user)[0].gender
    
    context = {
        'bits_data': bits_data,
        'bits_data1': bits_data1,
        
    }
    return render(request, 'bits.html',context)

def Ottawauni(request):
    ottawauni_data = Sprofile.objects.all().filter(user=request.user)[0].current_gpa
    ottawauni_data1 = Sprofile.objects.all().filter(user=request.user)[0].gender
    ottawauni_data2 = Sprofile.objects.all().filter(user=request.user)[0].speak_french

    
    context = {
        'ottawauni_data': ottawauni_data,
        'ottawauni_data1': ottawauni_data1,
        'ottawauni_data2': ottawauni_data2,
        
    }
    return render(request, 'UOttawauni.html',context)

def UofAuckland(request):
    auckland_data= Sprofile.objects.all().filter(user=request.user)[0].current_gpa
    auckland_data1= Sprofile.objects.all().filter(user=request.user)[0].gender
    auckland_data2= Sprofile.objects.all().filter(user=request.user)[0].sports

    context = {
        'auckland_data': auckland_data,
        'auckland_data1': auckland_data1,
        'auckland_data2': auckland_data2,
        
    }
    return render(request, 'UofAuckland.html',context)
def UIUCuni(request):
    uiu_data= Sprofile.objects.all().filter(user=request.user)[0].current_gpa
    uiu_data1= Sprofile.objects.all().filter(user=request.user)[0].sports

    context = {
        'uiu_data': uiu_data,
        'uiu_data1': uiu_data1,
        
    }
    return render(request, 'UIUCuni.html',context)

def Queenmary(request):
    queenmary_data= Sprofile.objects.all().filter(user=request.user)[0].current_gpa
    queenmary_data1= Sprofile.objects.all().filter(user=request.user)[0].sports
    queenmary_data2 = Sprofile.objects.all().filter(user=request.user)[0].gender

    context = {
        'queenmary_data': queenmary_data,
        'queenmary_data1': queenmary_data1,
        'queenmary_data2': queenmary_data2,
        
    }
    return render(request, 'Queenmary.html',context)

def Griffithuni(request):
    griffith_data= Sprofile.objects.all().filter(user=request.user)[0].current_gpa
    griffith_data1= Sprofile.objects.all().filter(user=request.user)[0].sports

    context = {
        'griffith_data': griffith_data,
        'griffith_data1': griffith_data1,
        
    }
    return render(request, 'Griffithuni.html',context)
from django.shortcuts import render
import requests

def generate_essay(request):
    api_key = "enter your api key"
    model = "text-davinci-002"
    prompt = "write me a proper application letter of 1000 for taking an admission in that university"

    response = requests.post(
        "https://api.openai.com/v1/completions",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
        json={
            "model": "text-davinci-002",
            "prompt": prompt,
            "temperature": 0.5,
            "max_tokens": 4000,
        },
    )
    

    essay = response.json()["choices"][0]["text"]
    return render(request, "application.html", {"essay": essay})




def home(request):
    return render(request, 'home.html')
def scholarship(request):
    return render(request, 'scholarship.html')
def university(request):
    return render(request, 'university.html')
def about(request):
    return render(request, 'about.html')

# Create your views here.
@login_required(login_url= LOGIN_REDIRECT_URL)
def index(request):
    return render(request, 'home.html')


def signUp(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            if User.objects.filter(username=username).first():
                messages.warning(request, 'Username already taken!')
                return redirect('/signup')
            if User.objects.filter(email=email).first():
                messages.warning(request, 'Email already taken!')
                return redirect('/signup')
            
            user_obj = User.objects.create_user(username=username, email=email, password=password)

            # you can use at time of forgot password.
            # user_obj.set_password('newpassword)
            auth_token=str(uuid.uuid4())
            profile_obj = Profile.objects.create(user=user_obj, auth_token=auth_token)
        
            # send_mail
            msg = send_mail(
                subject = 'Activate your account',
                message = f'Here is the message click on the link to activate http://127.0.0.1:8000/verify/{auth_token}',
                from_email = EMAIL_HOST_USER,
                recipient_list = [email],
                fail_silently=False,
            )

            user_obj.save()
            profile_obj.save()

            print('Mail sent successfully')
            messages.success(request, "Account created successfully")
            return redirect('/token')

        except Exception as e:
            print(e)
            return redirect('/error')

        
    return render(request, 'signUp.html')


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username = username).first()

        if user_obj is None:
            messages.warning(request, "User not found")
            return redirect("/login")     

        profile_obj = Profile.objects.filter(user = user_obj).first()

        if not profile_obj.verified:
            messages.warning(request, "Profile not verified, check your mail.")
            return redirect("/login")

        user = authenticate(username=username, password=password)
        if user is None:
            messages.warning(request, "Invalid Credentials")
            return redirect("/login")

        auth_login(request, user)
        # add path of edit_profile here
        return redirect("/index")
    return render(request, 'login.html')


def send_token(request):
    return render(request, 'send_token.html')


def verify(request, slug):
    try:
        profile_obj = Profile.objects.filter(auth_token = slug).first()
        if profile_obj:
            if profile_obj.verified:
                messages.success(request, 'Account already verified')
                return redirect('/login')

            profile_obj.verified = True
            profile_obj.save()
            messages.success(request, 'Your account is now verified')
            return redirect('/login')
        else:
            return redirect('/error')
        
    except Exception as e:
        print(e)
        return redirect('/error')


def error(request):
    return render(request, "error.html")

    
def logoutUser(requests):
    logout(requests)
    messages.success(requests, 'Logged out successfully')
    return redirect('/login')

def forgetPassword(request):
    if request.method == "POST":
        email = request.POST.get('email')
    
        try:
            userObj = User.objects.filter(email=email).first()
            if userObj is None:
                messages.warning(request, "User not found")
                return redirect("/login")

            profileObj = Profile.objects.filter(user = userObj).first()
            if profileObj is None:
                messages.warning(request, "Internal Error")
                return redirect('/error')

            token = profileObj.auth_token
            msg = send_mail(
                subject = 'Reset your Password',
                message = f'Follow this link to reset your password http://127.0.0.1:8000/reset/{token}',
                from_email = EMAIL_HOST_USER,
                recipient_list = [email],
                fail_silently=False,
            )

            if msg==1:
                return render(request, "mail_forgetPass.html")
            else:
                messages.warning(request, "Something went wrong! Try again later.")
                return redirect('/error')

        except Exception as e:
            print(e)
            return redirect('/error')

    return render(request, "forgetPass.html")


def reset(request, token):
    try:
        if request.method == "POST":
            new_password = request.POST.get('password1')
            confirm_password = request.POST.get('password2')

            if new_password == confirm_password:
                # print(confirm_password)

                profile_obj = Profile.objects.filter(auth_token = token).first()
                
                if profile_obj is None:
                    messages.warning(request, "Something went wrong!")
                    return redirect("/error") 

                user_id = profile_obj.user.id

                if user_id is None:
                    messages.warning(request, "User not found :(")
                    return redirect("/login")

                user_obj = User.objects.get(id = user_id)
                user_obj.set_password(new_password)
                user_obj.save()

                messages.success(request, "Password updated successfully :)")
                return redirect("/login")

            else:
                messages.warning(request, "Passwords doesn't match, enter again")


        # if user_obj:
            # print(user_obj.username)
        #     if profile_obj.verified:
        #         messages.success(request, 'Account already verified')
        #         return redirect('/login')

        #     profile_obj.verified = True
        #     profile_obj.save()
        #     messages.success(request, 'Your account is now verified')
        #     return redirect('/login')
        # else:
        #     return redirect('/error')
        
    except Exception as e:
        print(e)
        # return redirect('/error')

    return render(request, 'PassInput.html')
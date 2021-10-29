from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User,auth

# Create your views here.
def home(request):
  return render(request,'dashboard.html')

def stateLevel(request):
  return render(request,'statelevel.html')

def blockLevel(request):
  return render(request,'blocklevel.html')

def schoolLevel(request):
  return render(request,'schoollevel.html')

def districtLevel(request):
  return render(request,'districtlevel.html')

def login(request):
  if request.method == "POST":
    print("request = ",request)
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth.authenticate(username=username,password=password)
    if user is not None:
      auth.login(request,user)
      return render(request,'schoollevel.html')
    else:
      pass
  return render(request,'login.html')
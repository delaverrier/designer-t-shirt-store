from django.shortcuts import render
from django.contrib.auth.models import User
from django.db import models
#index это главная страница
def index(request):
    return render(request,'main/index.html')

def lovers(request):
    return render(request,'main/lovers.html')

def bones(request):
    return render(request,'main/bones.html')

def devil(request):
    return render(request,'main/devil.html')

def cart(request):
    return render(request,'main/cart.html')

def about(request):
    return render(request,'main/about.html')

from django.shortcuts import render, redirect

def index(request):
    return render(request, 'main/index.html')
def cart(request):
    return render(request, 'main/cart.html')
def lovers(request):
    return render(request, 'main/lovers.html')
def bones(request):
    return render(request, 'main/bones.html')

def devil(request):
    return render(request, 'main/devil.html')

def about(request):
    return render(request, 'main/about.html')

def service(request):
    return render(request, 'main/service.html')

def contacts(request):
    return render(request, 'main/contacts.html')

def login(request):
    return render(request, 'main/login.html')
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import *
from .models import *


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
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Перенаправление на домашнюю страницу после успешной аутентификации
    else:
        form = AuthenticationForm(request)
    return render(request, 'main/login.html', {'form': form})


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        return response

class LoginUser(LoginView):
    template_name = 'main/login.html'
    success_url = reverse_lazy('home')

class LogoutUser(LogoutView):
    next_page = reverse_lazy('login')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')  # перенаправляем пользователя на страницу входа после успешной регистрации
    else:
        form = UserCreationForm()
    return render(request, 'main/register.html', {'form': form})

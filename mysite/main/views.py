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
from .forms import ProfileForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import Product, CartItem
from django.contrib.auth import get_user
import uuid
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.sessions.models import Session
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
def index(request):
    return render(request, 'main/index.html')
def cart(request):
    return render(request, 'main/cart.html')
def lovers(request):
    product = Product.objects.get(pk=1)
    return render(request, 'main/lovers.html',{'item': product})
def bones(request):
    product = Product.objects.get(pk=2)
    return render(request, 'main/bones.html',{'item': product})

def devil(request):
    product = Product.objects.get(pk=3)
    return render(request, 'main/devil.html', {'item': product})


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
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # перенаправляем пользователя на страницу входа после успешной регистрации
    else:
        form = RegisterUserForm()
    return render(request, 'main/register.html', {'form': form})

@login_required
def profile(request):
    user = request.user
    profile = user.profile if hasattr(user, 'profile') else None

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)

    context = {
        'form': form,
        'profile': profile
    }
    return render(request, 'main/profile.html', context)

@login_required
def edit_profile(request):
    user = request.user
    profile = user.profile if hasattr(user, 'profile') else None

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        if profile:
            form = ProfileForm(instance=profile)
        else:
            form = ProfileForm()

    context = {
        'form': form,
        'profile': profile
    }
    return render(request, 'main/edit_profile.html', context)


def casino(request):
    return render(request, 'main/casino.html')


def add_to_cart(request, product_id):
    user_id = request.session.get('user_id')
    if not user_id:
        user = User.objects.create_user(username=str(uuid.uuid4()), password='')
        user_id = user.id
        request.session['user_id'] = user_id

    product = get_object_or_404(Product, pk=product_id)

    try:
        cart_item = CartItem.objects.get(product=product, user_id=user_id)
        cart_item.quantity += 1
    except CartItem.DoesNotExist:
        cart_item = CartItem(product=product, user_id=user_id, quantity=1, price=product.price)

    cart_item.subtotal = cart_item.quantity * cart_item.price
    cart_item.save()

    return redirect('cart')


def cart(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = User.objects.get(id=user_id)
        cart_items = CartItem.objects.filter(user=user)
    else:
        cart_items = []

    total = sum(item.subtotal for item in cart_items)
    return render(request, 'main/cart.html', {'cart_items': cart_items, 'total': total})


def clear_cart(request):
    user_id = request.session.get('user_id')
    if not user_id:
        user = User.objects.create_user(username=str(uuid.uuid4()), password='')
        user_id = user.id
        request.session['user_id'] = user_id

    CartItem.objects.filter(user_id=user_id).delete()

    return redirect('cart')


def payment_view(request):
    if request.method == 'POST':
        shipping_address = request.POST.get('shipping_address_input')
        payment_method = request.POST.get('payment_method')
        total = request.POST.get('total')

        recipient_name = request.POST.get('recipient_name')
        country = request.POST.get('country')
        street_house_apartment = request.POST.get('street_house_apartment')
        region = request.POST.get('region')
        city = request.POST.get('city')
        postal_code = request.POST.get('postal_code')
        mobile_phone = request.POST.get('mobile_phone')

        print('Адрес доставки:', shipping_address)
        print('Метод оплаты:', payment_method)
        print('Итого:', total)

        if payment_method == 'mastercard':
            return render(request, 'main/payment.html', {
                'total': total,
                'shipping_address': shipping_address,
                'payment_method': 'Mastercard',
                'recipient_name': recipient_name,
                'country': country,
                'street_house_apartment': street_house_apartment,
                'region': region,
                'city': city,
                'postal_code': postal_code,
                'mobile_phone': mobile_phone
            })
        elif payment_method == 'bitcoin':
            return render(request, 'main/payment.html', {
                'total': total,
                'shipping_address': shipping_address,
                'payment_method': 'Bitcoin',
                'recipient_name': recipient_name,
                'country': country,
                'street_house_apartment': street_house_apartment,
                'region': region,
                'city': city,
                'postal_code': postal_code,
                'mobile_phone': mobile_phone
            })

    return render(request, 'main/payment.html')


def mastercard(request, total, shipping_address):
    context = {
        'total': total,
        'shipping_address': shipping_address
    }
    return render(request, 'main/mastercard.html', context)

def bitcoin(request, total, shipping_address):
    context = {
        'total': total,
        'shipping_address': shipping_address
    }
    return render(request, 'main/bitcoin.html', context)










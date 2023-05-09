from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
urlpatterns = [
    path('',views.index, name='home'),
    path('lovers/', views.lovers, name='lovers'),
    path('bones/',views.bones),
    path('devil/',views.devil),
    path('cart/', views.cart, name='cart'),
    path('about/',views.about),
    path('contacts/',views.contacts),
    path('service/',views.service),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page=reverse_lazy('home')), name='logout')
]

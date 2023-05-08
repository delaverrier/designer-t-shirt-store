from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('lovers/', views.lovers, name='lovers'),
    path('bones/',views.bones),
    path('devil/',views.devil),
    path('cart/', views.cart, name='cart'),
    path('about/',views.about),
    path('contacts/',views.contacts),
    path('service/',views.service),
    path('login/',views.login)
]

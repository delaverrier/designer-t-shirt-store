from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('lovers/',views.lovers),
    path('bones/',views.bones),
    path('devil/',views.devil),
    path('cart/',views.cart),
    path('about/',views.about)
]

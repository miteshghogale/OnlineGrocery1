from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='homepage'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('product-details/<int:pk>', productdetails, name='product-details'),
    path('logout', logout, name='logout'),
    path('add_to_cart', add_to_cart, name='add_to_cart'),
    path('show_cart', show_cart, name='show_cart'),
    
]

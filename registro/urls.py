from django.urls import path 
from . import views
from django.shortcuts import render

#importar user
from django.contrib.auth.models import User
#sistema de autenticación 
from django.contrib.auth import authenticate,logout,login 
from django.contrib.auth.decorators import login_required

urlpatterns =[
    path('',views.home,name="home"),
    path('contact/',views.contact, name="contact"),
    path('Service/',views.servise,name="service"),
    path('tourism/',views.tourism,name="tourism"),
    path('singup/',views.singup, name="singup"),
    path('login/',views.login, name="login"),
    path('login/iniciar',views.login_iniciar,name="iniciar"),
    path('singup/crear', views.crear_U, name="crear"),
    

]
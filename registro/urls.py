from django.urls import path 
from . import views
from django.shortcuts import render

#importar user
from django.contrib.auth.models import User
#sistema de autenticación 
from django.contrib.auth import authenticate,logout, login as auth_login
from django.contrib.auth.decorators import login_required

urlpatterns =[
    path('',views.home,name="home"),
    path('registro/templates/Home.html',views.home,name="home"),
    path('registro/templates/contact.html',views.contact, name="contact"),
    path('registro/templates/Service.html',views.servise,name="service"),
    path('registro/templates/tourism.html',views.tourism,name="tourism"),
    path('registro/templates/singup.html',views.singup, name="singup"),
    path('registro/login.html',views.login, name="login"),
    path(r'^login/iniciar/$',views.login_iniciar,name="iniciar"),
    path('registro/crear', views.crear_U, name="crear")

]
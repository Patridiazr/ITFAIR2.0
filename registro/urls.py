from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static
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
    path('logout/',views.logout_view, name="logout"),
    path('mantenedor/',views.listado, name="mantenedor"),
    path('mantenedor/eliminarU/<int:id_u>', views.eliminar_U, name="eliminarU"),
    path('mantenedor/agregarT',views.crear_T, name="agregarT"),
    path('mantenedor/editarT/<int:id_t>',views.editar_T, name="editarT"),
    path('mantenedor/eliminarT/<int:id_u>', views.eliminar_T, name="eliminarT"),
    path('mantenedor/agregarS',views.crear_S, name="agregarS"),
    path('mantenedor/editarS/<int:id_s>',views.editar_S, name="editarS"),
    path('mantenedor/eliminarS/<int:id_u>', views.eliminar_S, name="eliminarS")        
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
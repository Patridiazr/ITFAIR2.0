from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render
from django.conf.urls import url
from django.contrib.auth import views as auth_views
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
    path('mensajes/',views.mensaje, name="mensajes"),
    path('login/',views.login, name="login"),
    path('login/iniciar',views.login_iniciar,name="iniciar"),
    path('singup/crear', views.crear_U, name="crear"),
    path('contact/enviar',views.crear_M, name="enviar"), 
    path('logout/',views.logout_view, name="logout"),
    path('mantenedor/',views.listado, name="mantenedor"),
    path('mantenedor/eliminarU/<int:id_u>', views.eliminar_U, name="eliminarU"),
    path('mantenedor/agregarT',views.crear_T, name="agregarT"),
    path('mantenedor/editarT/<int:id_t>',views.editar_T, name="editarT"),
    path('mantenedor/eliminarT/<int:id_t>', views.eliminar_T, name="eliminarT"),
    path('mantenedor/agregarS',views.crear_S, name="agregarS"),
    path('mantenedor/editarS/<int:id_s>',views.editar_S, name="editarS"),
    path('mantenedor/eliminarS/<int:id_s>', views.eliminar_S, name="eliminarS"),
    url(r'^contrasenia/$',views.contrasenia,name="contrasenia"),
    url(r'^contrasenia/$',views.cambio_contrasenia,name="cambio"),
    url(r'^password/recovery/$',
        auth_views.PasswordResetView.as_view(
            template_name='password_reset_form.html',
            html_email_template_name='password_reset_email.html',
        ),
        name='passwordreset',
    ),
    url(
        r'^password/recovery/(?P<uidb64>[0-9A-Za-z-]+)/'
        r'(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(
            success_url='/login/',
            post_reset_login=True,
            template_name='password_reset_confirm.html',
            post_reset_login_backend=(
                'django.contrib.auth.backends.AllowAllUsersModelBackend'
            ),
        ),
        name='password_reset_confirm',
    ),
    url(
        r'^password/recovery/done/$',
        auth_views.PasswordResetDoneView.as_view(
            template_name='password_reset_done.html',
        ),
        name='password_reset_done',

    ),
    url(r'^home/$',views.home, name="home")
  
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
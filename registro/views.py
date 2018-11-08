from django.shortcuts import render, redirect
from .models import Usuario, Mensaje
from django.contrib.auth import authenticate,login as auth_login
from django.http import HttpResponse



# Create your views here.

def home(request):
    return render(request,"home.html")

def servise(request):
    return render(request,"service.html")

def contact(request):
    return render(request,"contact.html")

def tourism(request):
    return render(request,"tourism.html")

def singup(request):
    return render(request,"singup.html")
    
def login(request):
    return render(request,"login.html")


def crear_U(request):
    correo = request.POST.get('email')
    contra = request.POST.get('psw')
    username = request.POST.get('')
    rut = request.POST.get('dni')
    nombre = request.POST.get('name')
    nacionalidad = request.POST.get('nationality')
    usu = Usuario(correo=correo, contra=contra, rut=rut, nombre=nombre, nacionalidad=nacionalidad)
    usu.save()
    user = User.objects.create_user(username,correo,contra)
    user.save()
    return redirect('login.html')

def crear_M(request):
    correo = request.POST.get('')
    mensaje = request.POST.get('menssage')
    org = request.POST.get('org')
    celu = request.POST.get('phone')
    nombre = request.POST.get('name')
    men = Mensaje(correo=correo, orga=org, mensaje=mensaje, nombre=nombre, celu=celu)
    men.save()
    return redirect('contact.html')

def login_iniciar(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = authenticate(request,username=username, password=password)
    print(username,password)
    if user is not None:
        auth_login(request, user)
        return HttpResponse('<script>alert("Inicio de sesión correcto."); window.location.href="home";</script>')
    else:
        return HttpResponse('<script>alert("Ocurrió un error, intenta nuevamente..."); window.location.href="/registro/login.html";</script>')


def eliminar_U(request, id_p):
    usuario = Usuario.objects.get(id=id_p)
    usuario.delete()
    return redirect('Listado')
        return HttpResponse('<script>alert("Ocurrió un error, intenta nuevamente..."); window.location.href="/..";</script>')

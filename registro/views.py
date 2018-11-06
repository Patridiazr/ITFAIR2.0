from django.shortcuts import render
from .models import Usuario, Mensaje

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
    rut = request.POST.get('dni')
    nombre = request.POST.get('name')
    nacionalidad = request.POST.get('nationality')
    usu = Usuario(correo=correo, contra=contra, rut=rut, nombre=nombre, nacionalidad=nacionalidad)
    usu.save()
    return redirect('login')

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
    usuario = request.POST.get('dni','')
    password = request.POST.get('password','')
    user = authenticate(request,username=usuario, password=password)
    if user is not None:
        auth_login(request, user)
        return HttpResponse('<script>alert("Inicio de sesión correcto."); window.location.href="/index/";</script>')
    else:
        return HttpResponse('<script>alert("Ocurrió un error, intenta nuevamente..."); window.location.href="/login/";</script>')

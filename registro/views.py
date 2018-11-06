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


def crear_U(request):
    correo = request.POST.get()
    contra = request.POST.get()
    usu = Usuario(correo=correo, contra=contra)
    usu.save()
    return redirect('login')

def crear_M(request):
    correo = request.POST.get('')
    mensaje = request.POST.get('menssage')
    org = request.POST.get('org')
    celu = request.POST.get('phone')
    nombre = request.POST.get('name')
    men = Mensaje(correo=correo, orga=org, mensaje=mensaje, nombre=nombre, celu=celu)
    me.save()
    return redirect('contact.html')

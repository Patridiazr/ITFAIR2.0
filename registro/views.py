from django.shortcuts import render, redirect
from .models import Usuario, Mensaje, Turistico, Servicios
from django.contrib.auth import logout, authenticate, login as auth_login
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.core.mail import EmailMessage





#LINKS
def home(request):
    return render(request,"home.html")

def servise(request):
    ser = Servicios.objects.all()
    context = {'servicios': ser}
    return render(request,"service.html",context)

def contact(request):
    return render(request,"contact.html")

def tourism(request):
    tur = Turistico.objects.all()
    context = {'turistico': tur}
    return render(request,"tourism.html",context)

def mensaje(request):
    men = Mensaje.objects.all()
    context = {'mensajes': men}
    return render(request,"mensajes.html",context)

def singup(request):
    return render(request,"singup.html")
    
def login(request):
    return render(request,"login.html")

def contrasenia(request):
    return render(request,'contraseña.html')

def listado(request):
    usuario = Usuario.objects.all()
    contexto3 = {'usuario': usuario}
    turistico = Turistico.objects.all()
    contexto1 = {'turistico':turistico}
    servicios = Servicios.objects.all()
    contexto2 = {'servicios':servicios}
    contexto ={'usuario':usuario,'turistico':turistico,'servicios':servicios}
    return render (request, 'mantenedor.html',contexto)   
    
#LOGIN

def login_iniciar(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = authenticate(request,username=username, password=password)
    print(username,password)
    if user is not None:
        auth_login(request, user)
        return HttpResponse('<script>alert("Inicio de sesión correcto."); window.location.href="/";</script>')
    else:
        return HttpResponse('<script>alert("Ocurrió un error, intenta nuevamente..."); window.location.href="/";</script>')

def logout_view(request):
    logout(request)
    return redirect('home')

#CRUD USUARIO
def crear_U(request):
    correo = request.POST.get('email')
    contra = request.POST.get('psw')
    username = request.POST.get('username')   
    nacionalidad = request.POST.get('nationality')
    usu = Usuario(correo=correo, contra=contra, nacionalidad=nacionalidad)
    usu.save()
    user = User.objects.create_user(username=username,email=correo,password=contra)
    user.save()
    return redirect('login')

def eliminar_U(request, id_u):
    usuario = Usuario.objects.get(id=id_u)
    usuario.delete()
    return redirect('mantenedor')

#CRUD MENSAJE +

def crear_M(request):
    correo = request.POST.get('email') 
    mensaje = request.POST.get('message')    
    telefono = request.POST.get('phone')
    nombre = request.POST.get('name')
    men = Mensaje(correo=correo, mensaje=mensaje, nombre=nombre, telefono=telefono)
    men.save()
    return redirect('contact')



#CRUD TURISTICO

def crear_T(request):
    titulo = request.POST.get('titulo')
    subtitulo = request.POST.get('subtitulo')
    foto  = request.FILES.get('foto', False)
    descripcion  = request.POST.get('descripcion')    
    tur = Turistico(titulo=titulo, subtitulo=subtitulo, foto=foto, descripcion=descripcion)
    tur.save()
    return redirect('mantenedor')

def editar_T(request,id_t):
    tur = Turistico.objects.get(pk=id_t)
    titulo = request.Post.get('titulo')
    foto  = request.Post.get('foto')
    descripcion  = request.Post.get('descripcion')
    tur.titulo=titulo
    tur.foto=foto
    tur.descripcion=descripcion
    tur.save()
    return redirect('mantenedor')

def eliminar_T(request, id_t):
    tutistico = Turistico.objects.get(id=id_t)
    tutistico.delete()
    return redirect('mantenedor')

#CRUD SERVICIOS

def crear_S(request):
    nombre = request.POST.get('nombre')
    titulo = request.POST.get('titulo')
    archivo = request.FILES.get('archivo')
    downl = request.POST.get('descripcion1')
    descripcion = request.POST.get('descripcion2')
    ser=Servicios(nombre=nombre, titulo=titulo, archivo=archivo, downl=downl, descripcion=descripcion)
    ser.save()
    return redirect('mantenedor')

def editar_S(request, id_s):
    ser = Servicios.objects.get(pk=id_s)
    nombre = request.Post.get('nombre')
    titulo = request.Post.get('titulo')
    link = request.Post.get('link')
    downl = request.Post.get('downl')
    descripcion = request.Post.get('descripcion')
    ser.nombre=nombre
    ser.titulo=titulo
    ser.link=link
    ser.downl=downl
    ser.descripcion=descripcion
    ser.save()
    return redirect('mantenedor')

def eliminar_S(request, id_s):
    servicios = Servicios.objects.get(id=id_s)
    servicios.delete()
    return redirect('mantenedor')


def cambio_contrasenia(request):
    contrasenia = request.POST.get('contrasenia','')
    persona.contrasenia = contrasenia
    persona.save()
    return redirect('/index/')

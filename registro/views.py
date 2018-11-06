from django.shortcuts import render

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

def login_iniciar(request):
    usuario = request.POST.get('dni','')
    password = request.POST.get('password','')
    user = authenticate(request,username=usuario, password=password)
    if user is not None:
        auth_login(request, user)
        return HttpResponse('<script>alert("Inicio de sesión correcto."); window.location.href="/index/";</script>')
    else:
        return HttpResponse('<script>alert("Ocurrió un error, intenta nuevamente..."); window.location.href="/login/";</script>')
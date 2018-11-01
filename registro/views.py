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
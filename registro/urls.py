from django.urls import path 
from . import views

urlpatterns =[
    path('',views.home,name="home"),
    path('registro/templates/Home.html',views.home,name="home"),
    path('registro/templates/contact.html',views.contact, name="contact"),
    path('registro/templates/Service.html',views.servise,name="service"),
    path('registro/templates/tourism.html',views.tourism,name="tourism")
]
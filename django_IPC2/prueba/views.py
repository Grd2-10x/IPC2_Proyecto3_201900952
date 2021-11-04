
from django.shortcuts import render
from django.template import Template, Context
posts = [
    {
        'autor':'Gerardo Luna',
        'titulo':'Laboratorio IPC2',
        'contenido':'probando Django',
        'fecha_post':'2021'
    }]
# Create your views here.
def home(request):
    usuario = 'admin'
    contexto = {
        'posts':posts,
        'user':usuario
    }
    return render(request, 'inicio.html', contexto)
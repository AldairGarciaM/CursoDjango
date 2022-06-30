from django.shortcuts import render, HttpResponse

# Create your views here.


def cursos(request):
    return render(request, "contenido/cursos.html")

def contacto(request):
    return render(request, "contenido/contacto.html")

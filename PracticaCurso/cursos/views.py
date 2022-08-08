from django.shortcuts import render
from .models import Cursos, comentarioContacto, Archivos
from .forms import comentarioContactoForm, formArchivo
from django.shortcuts import get_object_or_404
from django.contrib import messages

# Create your views here.
def cursos(request):
    cursos= Cursos.objects.all()

    return render(request, "cursos/principal.html", {'cursos': cursos})

def contacto(request):
    return render(request, 'cursos/contacto.html')

def registrar(request):
    if request.method == 'POST':
        form = comentarioContactoForm(request.POST)
        if form.is_valid(): 
            form.save()
            mensajes= comentarioContacto.objects.all()
            return render(request, 'cursos/comentarios.html', {'mensajes': mensajes})
    form = comentarioContactoForm()
    return render(request, 'cursos/contacto.html', {'form': form})

def mensajes(request):
    mensajes= comentarioContacto.objects.all()
    return render(request, 'cursos/comentarios.html', {'mensajes': mensajes})


def eliminarMensaje(request, id, confirmacion= 'cursos/eliminar.html'):
    comentario = get_object_or_404(comentarioContacto, id=id)
    if request.method== 'POST':
        comentario.delete()
        mensajes= comentarioContacto.objects.all()
        return render(request, 'cursos/comentarios.html', {'mensajes': mensajes})

    return render(request, confirmacion, {'object': comentario})


def archivos(request):
    if request.method=='POST':
        form= formArchivo(request.POST, request.FILES)
        if form.is_valid():
            titulo=request.POST['titulo']
            descripcion= request.POST['descripcion']
            archivo= request.FILES['archivo']
            insert= Archivos(titulo=titulo, descripcion=descripcion, archivo=archivo)
            insert.save()
            return render(request, "cursos/archivos.html")
        else:
            messages.error(request, "Error al procesar el archivo.")
    else:
        return render(request, "cursos/archivos.html", {'archivo': Archivos})
        
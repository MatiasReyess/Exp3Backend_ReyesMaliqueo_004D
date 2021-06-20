from django.shortcuts import render ,redirect
from .models import ComenUsuario 
from .forms import ComentarioForm

# Create your views here.

def index(request):
    return render(request, 'index1.html')
    
def galeria(request):
    return render(request, 'galeriaImagenes.html')

def mostrar(request):
    comentarios= ComenUsuario.objects.all()
    return render(request,'core/seccionComentarios.html',{'comentarios':comentarios})

def form_subir(request):
    if request.method == 'POST':
        comentario_form = ComentarioForm(request.POST)
        if comentario_form.is_valid():
            comentario_form.save()
            return redirect('mostrar')
    else:
        comentario_form = ComentarioForm()
    return render(request,'core/subirComentarios.html',{'comentario_form':comentario_form})

def modcomen(request,id):
    comentario = ComenUsuario.objects.get(idUser=id)
    datos ={
        'form': ComentarioForm(instance=comentario)
    }
    if request.method == 'POST':
        formulario = ComentarioForm(data=request.POST, instance = comentario)
        if formulario.is_valid:
            formulario.save()
            return redirect('mostrar')
    return render(request,'core/mod_comentarios.html',datos)

def delete_comen(request,id):
    comentario = ComenUsuario.objects.get(idUser=id)
    comentario.delete()
    return redirect('mostrar')
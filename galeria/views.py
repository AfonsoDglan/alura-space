from django.shortcuts import render, get_object_or_404, redirect
from galeria.models import Fotografia
from .forms import FotografiaForms


def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    fotografias = Fotografia.objects.order_by("horaCadastro").filter(publicado=True)
    return render(request, 'index.html', {"cards": fotografias})


def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'imagem.html', {"fotografia": fotografia})


def busca(request):
    if not request.user.is_authenticated:
        return redirect('login')
    fotografias = Fotografia.objects.order_by("horaCadastro").filter(publicado=True)
    if "busca" in request.GET:
        nome_busca = request.GET['busca']
        if nome_busca:
            fotografias = fotografias.filter(nome__icontains=nome_busca)
    return render(request, "busca.html", {"cards": fotografias})


def novaImagem(request):
    if not request.user.is_authenticated:
        return redirect('login')
    form = FotografiaForms()
    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'nova_imagem.html', {"form": form})


def editarImagem(request, foto_id):
    foto = Fotografia.objects.get(id=foto_id)
    form = FotografiaForms(instance=foto)
    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES, instance=foto)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'editar_imagem.html', {"form": form, "foto_id": foto_id})


def deletarImagem(request, foto_id):
    foto = Fotografia.objects.get(id=foto_id)
    foto.delete()
    return redirect('index')

from django.shortcuts import render, redirect, get_object_or_404
from .models import CarteiraEstudante
from .forms import CarteiraForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def cadastrar_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') 
    else:
        form = UserCreationForm()
    return render(request, 'registrar.html', {'form': form})

@login_required
def detalhe_carteira(request, pk):
    carteira = get_object_or_404(CarteiraEstudante, pk=pk)
    return render(request, 'exibir.html', {'carteira': carteira})

@login_required
def lista_carteiras(request):
    carteiras = CarteiraEstudante.objects.all()
    return render(request, 'lista.html', {'carteiras': carteiras})

@login_required
def criar_carteira(request):
    if request.method == 'POST':
        form = CarteiraForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_carteiras')
    else:
        form = CarteiraForm()
    return render(request, 'cadastrar.html', {'form': form})
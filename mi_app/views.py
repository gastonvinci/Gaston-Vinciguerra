from django.shortcuts import render, redirect
from .forms import CategoriaForm, ProductoForm, ClienteForm
from .models import Producto

def index(request):
    return render(request, 'mi_app/index.html')

def buscar(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        resultados = Producto.objects.filter(nombre__icontains=query)
        return render(request, 'mi_app/buscar.html', {'resultados': resultados})

def agregar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CategoriaForm()
    return render(request, 'mi_app/agregar_categoria.html', {'form': form})

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductoForm()
    return render(request, 'mi_app/agregar_producto.html', {'form': form})

def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ClienteForm()
    return render(request, 'mi_app/agregar_cliente.html', {'form': form})


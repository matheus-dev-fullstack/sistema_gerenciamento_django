from django.shortcuts import render
from .models import Categoria

def add_produto(request):
    if request.method == "GET":
        categoria = Categoria.objects.all()
        return render(request, 'add_produto.html', {'categorias': categoria})
    elif request.method == "POST":
        nome =request.

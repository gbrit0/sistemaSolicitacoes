# Lógica pro trás das rotas
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from home.models import Fotografia

def index(request):
   fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
   return render(request, 'home/index.html', {"cards": fotografias})

def imagem(request, foto_id):
   fotografia = get_object_or_404(Fotografia, pk=foto_id)
   return render(request, 'home/imagem.html',{"fotografia": fotografia})


def buscar(request):
   fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
   
   if "buscar" in request.GET:
      nome_a_buscar = request.GET['buscar']

      if nome_a_buscar:
         fotografias = fotografias.filter(nome__icontains=nome_a_buscar)
   return render(request, "home/buscar.html", {"cards": fotografias})
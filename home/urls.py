from django.urls import path
from home.views import index, imagem

urlpatterns = [
   path('', index, name='index'),
   path('imagem/', imagem, name='imagem')
]
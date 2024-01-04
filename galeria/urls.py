from django.urls import path
from galeria.views import index, imagem, busca, novaImagem, editarImagem, deletarImagem

urlpatterns = [
    path('', index, name="index"),
    path('imagem/<int:foto_id>', imagem, name="imagem"),
    path('buscar', busca, name="busca"),
    path('nova-imagem', novaImagem, name="novaImagem"),
    path('editar-imagem/<int:foto_id>', editarImagem, name="editarImagem"),
    path('deletar-imagem/<int:foto_id>', deletarImagem, name="deletarImagem"),
]

from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.cadastrar_usuario, name='registrar'),
    path('criar/', views.criar_carteira, name='criar_carteira'),
    path('listar/', views.lista_carteiras, name='lista_carteiras'),
    path('exibir/<int:pk>/', views.detalhe_carteira, name='detalhe_carteira'),
]
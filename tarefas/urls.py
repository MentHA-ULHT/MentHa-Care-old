from django.urls import path
from . import views


urlpatterns = [
    path('lista', views.listar_tarefas),
    path('nova', views.nova_tarefa),
]
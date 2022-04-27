from diario import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('nova_nota', views.nova_nota, name='nova_nota'),
    path('listar_participantes', views.listar_participantes, name='listar_participantes'),
    path('listar_notas/<int:id>', views.listar_notas, name='nova_nota'),
]
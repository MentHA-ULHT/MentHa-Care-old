from diario import views
from django.urls import path

urlpatterns = [
    path('care_grupos', views.view_care_grupos, name='care_grupos'),
    path('cog_grupos', views.view_cog_grupos, name='cog_grupos'),
    path('avalia_grupos', views.view_avalia_grupos, name='avalia_grupos'),
    path('participantes', views.view_participantes, name='participantes'),
    path('diario', views.view_diario, name='diario'),
    path('', views.view_diario),
    path('diario_participante/<int:id>', views.view_diario_participante, name='diario_participante'),
    path('diario_grupo/<int:idGrupo>', views.view_diario_grupo, name='diario_grupo'),
    path('presencas_sessao', views.view_presencas_sessao, name='presencas_sessao'),

    path('lista_sessoes', views.view_lista_sessoes, name='lista_sessoes'),

    path('menu_esquerda', views.view_menu_esquerda, name='menu_esquerda'),

]
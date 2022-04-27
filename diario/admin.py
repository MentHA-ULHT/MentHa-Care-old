from django.contrib import admin

# Register your models here.
from .models import Participante, Grupo, Dinamizador,Nota

admin.site.register(Participante)
admin.site.register(Grupo)
admin.site.register(Dinamizador)
admin.site.register(Nota)

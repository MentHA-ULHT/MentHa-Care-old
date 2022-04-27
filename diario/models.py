from django.db import models
from datetime import datetime

class Grupo(models.Model):
    nome = models.CharField(max_length=20)
    def __str__(self):
        return f'{self.nome}'

class Utilizador (models.Model):
    nome = models.CharField(max_length=20)
    class Meta:
        abstract = True

class Participante(Utilizador):
    data_nascimento = models.DateField(null=True, blank=True)
    local_nascimento = models.CharField(max_length=20, null=True, blank=True)
    diagnostico = models.CharField(max_length=20, null=True, blank=True)

    grupo = models.ForeignKey(
        Grupo,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name= 'participante'
        )

    def __str__(self):
        return f'{self.nome}'



class Dinamizador(Utilizador):
    grupo = models.ManyToManyField(Grupo, related_name='dinamizadores')
    def __str__(self):
        return f'{self.nome}'

class Nota(models.Model):
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE,)
    descricao = models.TextField(max_length=1000)
    data = models.DateTimeField(auto_now_add = True)
    sessao = models.CharField(max_length=10,default = "1")
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.descricao}"

class Partilha(models.Model):
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE, )
    descricao = models.CharField(max_length=1000)

class RegistoAutobiografico(models.Model):
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE,)
    fotografia = models.ImageField(max_length=30, null=True, blank=True)
    descricao = models.CharField(max_length=1000)
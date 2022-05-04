from django.db import models
from datetime import datetime

##### Eventos ######################################


class Evento(models.Model):
    data = models.DateTimeField()
    class Meta:
        abstract = True


"""class Lembrete(models.Model):
    data = models.DateTimeField()
    evento = models.ForeignKey(Evento)"""


class Sessao(Evento):
    nome = models.CharField(max_length=10)


class Exercicio(models.Model):
    nome = models.CharField(max_length=10)
    sessao = models.ManyToManyField(Sessao)
    materiais = models.CharField(max_length=1000)
    instrucao = models.CharField(max_length=1000)


# muitos tipos de utilizadores!
# cuidador tem paciente(es) e grupo. paciente tem cuidador(es) e grupo. dinamizador(es) tem grupo(s).

class Grupo(models.Model):
    nome = models.CharField(max_length=20)
    def __str__(self):
        return f'{self.nome}'
    class Meta:
        abstract = True


class GrupoCare(Grupo):
    def __str__(self):
        return f'{self.nome}'


class Utilizador (models.Model):
    nome = models.CharField(max_length=20)
    class Meta:
        abstract = True


class Cuidador(Utilizador):
    grupoCare = models.ManyToManyField(GrupoCare, blank=True, related_name='cuidadores')
    # blank=True permite que possa haver um cuidador sem grupo
    def __str__(self):
        return f'{self.nome}'


class Mentor(Utilizador):
    grupoCare = models.ManyToManyField(GrupoCare, blank=True, related_name='mentores')
    def __str__(self):
        return f'{self.nome}'


class DinamizadorConvidado(Utilizador):
    grupoCare = models.ManyToManyField(GrupoCare, blank=True, related_name='dinamizadores')
    def __str__(self):
        return f'{self.nome}'


###################################  COG ########################

class GrupoCog(Grupo):
    def __str__(self):
        return f'{self.nome}'


class Facilitador(Utilizador):
    grupoCog = models.ManyToManyField(GrupoCog, blank=True, related_name='facilitadores')
    def __str__(self):
        return f'{self.nome}'


class Auxiliar(Utilizador):
    grupoCog = models.ManyToManyField(GrupoCog, blank=True, related_name='auxiliares')
    def __str__(self):
        return f'{self.nome}'

###################################  Avalia ########################

class Avaliador(Utilizador):
    def __str__(self):
        return f'{self.nome}'


class Participante(Utilizador):
    grupoCog = models.ForeignKey(GrupoCog, on_delete=models.CASCADE, null=True, blank=True, related_name='participantes')
    cuidador = models.ManyToManyField(Cuidador, default="", blank=True, related_name='cuidadores')
    def __str__(self):
        return f'{self.nome}'


class Nota(models.Model):
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE)
    nota = models.TextField()
    data = models.DateTimeField(auto_now_add=True, null=True)
    # podemos ter alternativamente dois campos: criado, modificado sendo o segundo atualizado se modificada a nota
    # https://stackoverflow.com/questions/1737017/django-auto-now-and-auto-now-add

    def __str__(self):
        return f'{self.nota}'


class Partilha(models.Model):
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE)
    partilha = models.TextField()
    data = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.partilha}'

class Informacoes(models.Model):
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE)
    informacoes = models.TextField()
    data = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.partilha}'


class Respostas(models.Model):
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE)
    respostas = models.TextField()
    data = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.partilha}'




class GrupoAvalia(Grupo):
    avaliador = models.ForeignKey(Avaliador, on_delete=models.CASCADE)
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.nome}'
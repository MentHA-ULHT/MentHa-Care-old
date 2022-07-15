from django.db import models
from datetime import datetime

##### Eventos ######################################


class Evento(models.Model):
    data = models.DateTimeField()
    class Meta:
        abstract = True

class Sessao(Evento):
    PRESENT = 'P'
    ONLINE = 'O'
    MISTO = 'M'
    REGIME = [
        (PRESENT, "Presencial"),
        (ONLINE, "Online"),
        (MISTO,"Misto")
    ]
    PORREALIZAR = 'PR'
    REALIZADO = 'R'
    ESTADO = [
        (PORREALIZAR, "Por realizar"),
        (REALIZADO, "Realizado"),
    ]

    estado = models.CharField(max_length=20,choices=ESTADO, null=True, blank=True,default=PORREALIZAR)
    regime = models.CharField(max_length=20,choices=REGIME, null=True, blank=True,default=PRESENT)
    numeroSessao = models.CharField(max_length=10,null=True , blank=True)
    nome = models.CharField(max_length=100)
    introducao = models.TextField(max_length=1000, null=True, blank=True)
    instrucoes = models.TextField(max_length=1000, null=True, blank=True)
    tema = models.CharField(max_length=1000, null=True, blank=True)
    dinamizadores = models.CharField(max_length=1000, null=True, blank=True)
    componentes = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return f'{self.nome}'

class Exercicio(models.Model):
    INICIAL = 'I'
    DESENVOLVIMENTO = 'D'
    FINAL = 'F'
    FASE = [
        (INICIAL, "Inicial"),
        (DESENVOLVIMENTO, "Desenvolvimento"),
        (FINAL, "Final")
    ]
    nome = models.CharField(max_length=100)
    sessoes = models.ManyToManyField(Sessao, related_name='exercicios') # plural, pois um exercicio esta em varias sessoes!
    materiais = models.CharField(max_length=1000, null=True, blank=True)
    # Extra ?
    fase = models.CharField(max_length=10, choices=FASE, null=True, blank=True)
    duracao = models.CharField(max_length=10,null=True, blank=True)
    atividade = models.TextField(max_length=1000, null=True, blank=True)
    objetivo = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return f'{self.nome}'

class Grupo(models.Model):
    # participantes = models.ManyToManyField(Participante,related_name='grupos')

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
#criar class para o grupo e ir buscar a class participante da ines

class Nota(models.Model):
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE)
    nota = models.TextField()
    data = models.DateTimeField(auto_now_add=True, null=True)
    # podemos ter alternativamente dois campos: criado, modificado sendo o segundo atualizado se modificada a nota
    # https://stackoverflow.com/questions/1737017/django-auto-now-and-auto-now-add

    def __str__(self):
        return f'{self.nota}'

class NotaGrupo(models.Model):
    grupo = models.ForeignKey(GrupoCare, on_delete=models.CASCADE, null=True)
    notaGrupo = models.TextField()
    data = models.DateTimeField(auto_now_add=True, null=True)
    # podemos ter alternativamente dois campos: criado, modificado sendo o segundo atualizado se modificada a nota
    # https://stackoverflow.com/questions/1737017/django-auto-now-and-auto-now-add

    def __str__(self):
        return f'{self.notaGrupo}'

class Partilha(models.Model):
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE)
    partilha = models.TextField()
    data = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.partilha}'

class PartilhaGrupo(models.Model):
    grupo = models.ForeignKey(GrupoCare, on_delete=models.CASCADE)
    descricao = models.TextField()
    data = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.descricao}'

class Informacoes(models.Model):
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE)
    informacoes = models.TextField()
    data = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.informacoes}'


class Respostas(models.Model):
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE)
    pergunta = models.CharField(null=True, blank=True, max_length=1)
    respostas = models.TextField()
    data = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.respostas}'


class GrupoAvalia(Grupo):
    avaliador = models.ForeignKey(Avaliador, on_delete=models.CASCADE)
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.nome}'


                    # Criacao da class para o grupo

class InformacoesGrupo(models.Model):
    grupo = models.ForeignKey(GrupoCare, on_delete=models.CASCADE)
    descricao = models.TextField()
    data = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.descricao}'



class Presenca(models.Model):
    # Possibilidade de registar o motivo de noa ter ido a sessao
    PRESENT = 'P'
    ONLINE = 'O'
    PROTOCOLO ='PR'
    COG = 'CG'
    CARE = 'CR'
    MODES = [
        (PRESENT, "Presencial"),
        (ONLINE, "Online")
    ]
    SESSAO = [
        (PROTOCOLO, "Protocolo"),
        (COG, "Cog"),
        (CARE, "Care")
    ]
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE, null=True, blank=True,
                                      related_name='presencas')
    tipoSessao = models.CharField(choices=SESSAO, null=True, blank=True,default=CARE,max_length=20)
    sessao = models.ForeignKey(Sessao, on_delete=models.CASCADE, null=True, blank=True, related_name='sessao')
    # info a recolher no formulário, com checkboxes
    present = models.BooleanField(default= False)
    faltou = models.BooleanField(default=False)
    mode = models.CharField(max_length=20,choices=MODES, null=True, blank=True,default=PRESENT)
    withApp = models.BooleanField(null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)



from django.db import models

# Create your models here.


class Tarefa(models.Model):
    titulo = models.CharField(max_length=30)
    concluido = models.BooleanField(default = False)
    prioridade = models.IntegerField(default=3)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} | criado a: {self.data_criacao.date()} | prioridade: {self.prioridade}"
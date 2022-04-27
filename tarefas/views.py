from django.shortcuts import render
from .models import Tarefa
from .forms import TarefaForm
# Create your views here.

def listar_tarefas(request):
    lista_tarefas = sorted(Tarefa.objects.all(), key=lambda tarefa: tarefa.prioridade)
    context = {'tarefas': lista_tarefas}

    return render(request, 'tarefas/lista.html', context)


def nova_tarefa(request):
    form = TarefaForm(request.GET or None)
    if form.is_valid():
        form.save()

    context = {'form': form}

    return render(request, 'tarefas/nova.html', context)


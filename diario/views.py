from django.shortcuts import render
from .models import Grupo, Participante, Dinamizador, Nota
from .forms import NotaForm
from django.http import HttpResponse

# Create your views here.


def index(request):
    grupos = Grupo.objects.all()

    contexto = {
        'grupos': grupos,
    }

    return render(
        request,
        "diario/index.html",
        contexto
    )


def nova_nota(request):
    if request.method=='POST':
        print("\n\nfoi enviado algo\n\n")
        form = NotaForm(request.POST)
        if form.is_valid():
            print("\n\né valido. vai guardar\n\n")
            form.save()

    form = NotaForm()
    contexto = {'form': form}

    return render(request, "diario/nova_nota.html",  contexto)

def listar_participantes(request):
    return render(request, "diario/participantes.html", {'participantes': Participante.objects.all()})



def listar_notas(request, id):
    notas = Nota.objects.filter(participante=id)
    print(f'\n\n{notas}\n\n')
    return HttpResponse(f'{str(notas)}')


# necessario defenir o registo autobiografico ???

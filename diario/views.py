from django.shortcuts import render
from .models import GrupoCare, GrupoCog, GrupoAvalia, Participante, Nota, Partilha,Informacoes,PartilhaGrupo,Respostas,Presenca,NotaGrupo,Sessao,Exercicio
from django.http import HttpResponse
from .forms import NotaForm, PartilhaForm,InformacoesForm,RespostasForm,PartilhaGrupoForm,PresencaForm,NotaGrupoForm


# Create your views here.
def view_care_grupos(request):
    group_id = 1
    grupo = GrupoCog.objects.get(id=group_id)

    sessao_id = 1
    sessao = Sessao.objects.get(id=sessao_id)



    contexto = {'grupos': GrupoCare.objects.all(),
                'exercicios': sessao.exercicios.all(),
                'sessao': Sessao.objects.filter(id=sessao_id)

                }
    return render(request, "diario/care_grupos.html", contexto)

def view_cog_grupos(request):
    contexto = {'grupos': GrupoCog.objects.all()}
    return render(request, "diario/cog_grupos.html", contexto)

def view_avalia_grupos(request):
    contexto = {'grupos': GrupoAvalia.objects.all()}
    return render(request, "diario/avalia_grupos.html", contexto)

def view_participantes(request):
    contexto = {'grupos': GrupoCog.objects.all(), 'participantes': Participante.objects.all()}
    return render(request, "diario/participantes.html", contexto)




def view_lista_sessoes(request):

    group_id = 1
    grupo = GrupoCog.objects.get(id=group_id)

    sessao_id = 1
    sessao = Sessao.objects.get(id=sessao_id)
    gruposessa = Sessao.objects.all()



    contexto = {
        'participantes': Participante.objects.filter(grupoCog=group_id),
        'grupo': GrupoCog.objects.get(id=group_id),
        'exercicios': sessao.exercicios.all(),
        'gruposessao': gruposessa
    }

    return render(request, "diario/lista_sessoes.html", contexto)


def view_presencas_sessao(request):

    group_id = 1
    grupo = GrupoCog.objects.get(id=group_id)

    sessao_id = 1
    sessao = Sessao.objects.get(id=sessao_id)

    # unico usado é o participantes

    contexto = {
        'participantes': Participante.objects.filter(grupoCog=group_id),
        'grupo': GrupoCog.objects.get(id=group_id),
        'exercicios': sessao.exercicios.all(),
        'sessao': Sessao.objects.filter(id=sessao_id)
    }

    return render(request, "diario/presencas_sessao.html", contexto)



def view_diario(request):

    group_id = 1
    grupo = GrupoCog.objects.get(id=group_id)

    sessao_id = 1
    sessao = Sessao.objects.get(id=sessao_id)

    contexto = {
        'participantes': Participante.objects.filter(grupoCog=group_id),
        'grupo': GrupoCog.objects.get(id=group_id),
        'exercicios': sessao.exercicios.all(),
        'sessao': Sessao.objects.filter(id=sessao_id)
    }

    return render(request, "diario/diario.html", contexto)

def view_diario_participante(request, id):

    form = NotaForm(request.POST or None)
    if form.is_valid():
        form.save()

    form = PartilhaForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'participante_id': id,
        'notas': Nota.objects.filter(participante=id).order_by('-data'),
        'partilhas': Partilha.objects.filter(participante=id).order_by('-data'),
        'informacoes': Informacoes.objects.filter(participante=id).order_by('-data'),
        'respostas': Respostas.objects.filter(participante=id).order_by('-data'),
        'notaForm': NotaForm(),
        'partilhaForm': PartilhaForm()
    }

    return render(request, "diario/diario_participante.html", context)

def view_diario_grupo(request, idGrupo):
    form = NotaGrupoForm(request.POST or None)
    if form.is_valid():
        form.save()

    form = RespostasForm(request.POST or None)
    if form.is_valid():
        form.save()


    context = {
        'participantes': Participante.objects.filter(grupoCog=idGrupo).order_by('nome'),
        'grupo_id': idGrupo,
        'notasGrupo': NotaGrupo.objects.filter(grupo=idGrupo),
        'partilhas': PartilhaGrupo.objects.filter(grupo=idGrupo),
        'informacoes': Informacoes.objects.all(),
        'respostas': Respostas.objects.all(),
        'notaForm': NotaGrupoForm(),
        'partilhaGrupoForm': PartilhaGrupoForm()

    }

    return render(request, "diario/diario_grupo.html", context)


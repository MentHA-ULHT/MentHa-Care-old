from django.forms import ModelForm, TextInput, Textarea
from .models import Nota, Partilha,Informacoes,Respostas,NotaGrupo,PartilhaGrupo,Presenca

class NotaForm(ModelForm):
    class Meta:
        model = Nota
        fields = '__all__'
        widgets = {
            'nota': Textarea(attrs={'rows': 3, 'placeholder': 'Escreva uma nota...'}),
        }

class NotaGrupoForm(ModelForm):
    class Meta:
        model = NotaGrupo
        fields = '__all__'
        widgets = {
            'notaGrupo': Textarea(attrs={'rows': 3, 'placeholder': 'Escreva uma nota sobre o grupo...'}),
        }

class PartilhaForm(ModelForm):
    class Meta:
        model = Partilha
        fields = '__all__'
        widgets = {
            'partilha': Textarea(attrs={'rows': 3, 'placeholder': 'Escreva uma partilha...'}),
        }

class PartilhaGrupoForm(ModelForm):
    class Meta:
        model = PartilhaGrupo
        fields = '__all__'
        widgets = {
            'partilhaGrupo': Textarea(attrs={'rows': 3, 'placeholder': 'Escreva uma partilha sobre o grupo...'}),
        }

#Nova seccao

class InformacoesForm(ModelForm):
    class Meta:
        model = Informacoes
        fields = '__all__'
        widgets = {
            'Informacoes': Textarea(attrs={'rows': 3, 'placeholder': 'Escreva uma informacao...'}),
        }

class RespostasForm(ModelForm):
    class Meta:
        model = Respostas
        fields = '__all__'
        widgets = {
            'Respostas': Textarea(attrs={'rows': 3, 'placeholder': 'Escreva uma resposta...'}),
        }

class PresencaForm(ModelForm):
    class Meta:
        model = Presenca
        fields = '__all__'
        widgets = {
            'Presenca': Textarea(attrs={'rows': 3, 'placeholder': 'Escreva a Presenca'}),
        }
from django.forms import ModelForm, TextInput, Textarea
from .models import Nota, Partilha,Informacoes,Respostas


class NotaForm(ModelForm):
    class Meta:
        model = Nota
        fields = '__all__'
        widgets = {
            'nota': Textarea(attrs={'rows': 3, 'placeholder': 'Escreva uma nota...'}),
        }

class PartilhaForm(ModelForm):
    class Meta:
        model = Partilha
        fields = '__all__'
        widgets = {
            'partilha': Textarea(attrs={'rows': 3, 'placeholder': 'Escreva uma partilha...'}),
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
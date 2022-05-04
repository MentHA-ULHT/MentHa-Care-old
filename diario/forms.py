from django.forms import ModelForm, TextInput, Textarea
from .models import Nota, Partilha


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

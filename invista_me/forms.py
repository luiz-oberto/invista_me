from django.forms import ModelForm
from .models import Investimento

# o nome de uma classe de formulário deve seguir o padrão: class NomeDaCLasseForm. 
# sempre haverá o form no final
class InvestimentoForm(ModelForm):
    class Meta:
        model = Investimento
        fields = '__all__'
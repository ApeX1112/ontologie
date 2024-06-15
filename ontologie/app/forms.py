from django.forms import ModelForm
from .models import exercice 

class exoform(ModelForm):
    class Meta:
        model=exercice
        fields=[
            'nom_de_l_exercice',
            'type_d_exercice',
            'partie_de_corps_ciblée',
            'niveau',
            'description',
            'illustration',
        ]

from django.db import models

class exercice(models.Model):
    nom_de_l_exercice =models.CharField(max_length=200)
    type_d_exercice=models.CharField(max_length=200)
    partie_de_corps_ciblée=models.CharField(max_length=200)
    niveau=models.IntegerField()
    description=models.TextField()
    illustration=models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.nom_de_l_exercice

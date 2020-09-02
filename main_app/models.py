from django.db import models

from django.db import models
from django.urls import reverse

from django.conf import settings



class Arret(models.Model):
    identifiant = models.SlugField(primary_key=True)
    date = models.CharField(max_length=20)
    juridiction = models.CharField(max_length=200)
    page = models.IntegerField()
    contenu = models.TextField()
    selected = models.BooleanField(default=False)
    image = models.URLField()
    annee = models.IntegerField()
    num_receuil = models.IntegerField()

    #TODO
    def get_highlited(self):

        pass

    def get_selection_url(self):
        return reverse("core:select")

    def select(self):
        self.selected = not self.selected



#class Receuil(models.Model):
#    nom = models.CharField(max_length=150,blank=True, null=True)
#    arrets = models.ManyToManyField(Arret)
#




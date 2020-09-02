from django.db import models

from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.conf import settings
import re


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
    def highlights(self):
        text = self.contenu
        patterns = [r" évid\S+", r" abrog\S+", r" nécess\S+", r" n(e\s|')(\S+?\s){1,5}pas ", r"[a-zA-Z]+?(rais|rait|rions|riez|raient) "]
        for pattern in patterns:
          p = re.compile(pattern)
          count = 0
          for m in p.finditer(text):
            start, end = m.span()
            start += count*7
            end += count*7
            text = text[:start]+ "<b>" + text[start:end ] + "</b>" + text[end : ] 
            count += 1
        return mark_safe(text)

    def get_selection_url(self):

        return reverse("core:select", )

    def select(self):
        self.selected = not self.selected



#class Receuil(models.Model):
#    nom = models.CharField(max_length=150,blank=True, null=True)
#    arrets = models.ManyToManyField(Arret)
#




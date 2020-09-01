from django.shortcuts import render, redirect
from django.conf import settings
import os
import pandas as pd
from .models import Arret
# Create your views here.


def base(request):
    return render(request,"base.html")

def clear(request):
    Arret.objects.all().delete()
    return render(request,"base.html")



def load_in_db(request,slug):
    L = os.listdir(settings.CACHE_ROOT + "/" + slug)
    for id,csv_file in enumerate(L):

        df = pd.read_csv(settings.CACHE_ROOT + "/" + slug + "/" + csv_file, sep=";",index_col=0)

        #R = Receuil()
        #R.nom = slug + str(id)

        for arret, annee, juridiction, page, identifiant, image in zip(df["arrêt"], df["date"], df["juridiction"], df["page"],df.index,df["lien"]):

            A = Arret()
            A.date = annee
            A.annee = slug
            A.num_receuil = id
            A.page = page
            A.contenu = arret
            A.juridiction = juridiction
            A.image = image
            A.identifiant = identifiant
            A.save()

            #R.arrets.add(A)
            #R.save()


    return render(request, "loaded_success.html")

def suggestions_view(request,slug):
    context = {
        "datas":Arret.objects.filter(annee=slug)
    }
    return render(request, "suggestions_table.html",context=context)


def select_arret(request,slug):
    article_qs = Arret.objects.filter(identifiant=slug)
    if(article_qs.exists()):
        article = article_qs[0]
        article.selected = not article.selected
    return redirect("main:suggestions")
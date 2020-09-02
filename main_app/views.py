from django.shortcuts import render, redirect
from django.conf import settings
import os
import pandas as pd
from .models import Arret, Pattern
from django.db.models import Q
from django.views.generic import ListView
from .formulaire_home import form_patterns

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

#def suggestions_view(request,slug):
#    context = {
#        "datas":Arret.objects.filter(Q(contenu__regex = r" évid") | Q(contenu__regex = r" abrog")| Q(contenu__regex = r" nécess"), annee=slug)
#    }
#    return render(request, "suggestions_table.html",context=context)

class suggestions_view(ListView):
    template_name = "suggestions_table.html"
    paginate_by = 10

    def get_queryset(self):
        patterns = Pattern.objects.filter(selected = True)
        result = Arret.objects.none()
        for p in patterns:
            result = result | Arret.objects.filter(contenu__regex = p.pattern, annee = self.kwargs["slug"])

        
        return result


def select_arret(request,annee,slug):
    article_qs = Arret.objects.filter(identifiant=slug)
    if(article_qs.exists()):
        article = article_qs[0]
        article.selected = not article.selected
        article.save()
    return redirect("core:suggestions",slug=annee)
def load_patterns(request):
    for name, pattern in zip(["évidence", "abrogation", "nécessité", "négation", "conditionnel"] , [r" évid", r" abrog", r" nécess", r" n(e\s|')(\S+?\s){1,5}pas ", r"[a-zA-Z]+?(rais|rait|rions|riez|raient) "]):
        P = Pattern()
        P.name = name
        P.pattern = pattern
        P.selected = False
        P.save()
    return render(request, "loaded_success_patterns.html")

def get_choice(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = form_patterns(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # change the sleceted patterns in the DB
            pattern_names = form.cleaned_data.get('choice')
            Patterns = Pattern.objects.all()
            for p in Patterns:
                if p.name in pattern_names:
                    p.selected = True
                else:
                    p.selected = False
                p.save()

            year = form.cleaned_data.get('year')


            # redirect to a new URL:
            return redirect("core:suggestions", slug = year)

def home(request):
    Form = form_patterns()
    context = {"form" : Form}
    print("lala")
    return render(request, "home.html", context = context)


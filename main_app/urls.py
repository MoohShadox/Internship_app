from django.urls import path
from .views import base,suggestions_view, load_in_db,clear , select_arret
urlpatterns = [
    path("",base,name="base"),
    path("load_from_cache/<slug>",load_in_db,name="load-from-cache"),
    path("suggestions/<slug>", suggestions_view.as_view(), name="suggestions"),
    path("select/<annee>/<slug>", select_arret, name="select"),

    path("clear_db",clear,name="clear")
]

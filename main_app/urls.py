from django.urls import path
from .views import base,suggestions_view, load_in_db,clear , select_arret, load_patterns, get_choice, home
urlpatterns = [
    path("load_from_cache/<slug>",load_in_db,name="load-from-cache"),
    path("suggestions/<slug>", suggestions_view.as_view(), name="suggestions"),
    path("select/<slug>", select_arret, name="select"),

    path("clear_db",clear,name="clear"),
    path("load_patterns", load_patterns, name = "load_patterns"),
    path("get_choice", get_choice, name = "get_choice"),
    path("home", home, name="home")
]

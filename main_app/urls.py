from django.urls import path
from .views import base,suggestions_view, load_in_db,clear , select_arret
urlpatterns = [
    path("home", home, name="home")
    path("load_patterns", load_patterns, name="load_patterns"),
    path("load_from_cache/<slug>",load_in_db,name="load-from-cache"),
    path("suggestions/<slug>", suggestions_view.as_view(), name="suggestions"),
    path("select/<slug>", select_arret, name="select"),
    path("dl_csv", download_file, name="dl_csv"),
    path("clear_db",clear,name="clear"),
    path("get_choice", get_choice, name="get_choice"),
]

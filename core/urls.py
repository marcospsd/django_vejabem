from django.urls import path
from . import views



urlpatterns = [

    path("", views.PostListView.as_view(), name="index"),
    path("historico/", views.HistoricoListView.as_view(), name='historico'),
    path("videos/", views.YoutubeListView.as_view(), name='videos'),
    path("webinar/", views.WebinarListView.as_view(), name='webinar'),
    path("webinar/<post_id>", views.WebinarSlugView.as_view(), name='webinar'),
    path("posts/<post_id>", views.post),
    path("videos/<video_id>", views.videos),
    path("search/", views.searchpost, name='searchpost'),
    path("dimaiz/", views.DimaizView.as_view(), name='dimaiz'),
    path("circulares/", views.CircularesListView.as_view(), name='circulares'),
    path("circulares/<circular_id>", views.circular, name='circular_slug'),
    path("tabela_lentes/", views.TabelaLentesListView.as_view(), name='tabela_lentes'),
    path("tabela_lentes/<tabelapreco_id>", views.tabelapreco, name='tabela_lentes_slug'),


]

from django.urls import path
from . import views



urlpatterns = [
    path("", views.PostListView.as_view(), name="index"),
    path("historico/", views.HistoricoListView.as_view(), name='historico'),
    path("posts/<post_id>", views.post),
    path("search/", views.searchpost, name='searchpost'),

]

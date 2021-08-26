from django.urls import path
from . import views



urlpatterns = [

    path("", views.PostListView.as_view(), name="index"),
    path("historico/", views.HistoricoListView.as_view(), name='historico'),
    path("videos/", views.YoutubeListView.as_view(), name='videos'),
    path("posts/<post_id>", views.post),
    path("videos/<video_id>", views.videos),
    path("search/", views.searchpost, name='searchpost'),

]

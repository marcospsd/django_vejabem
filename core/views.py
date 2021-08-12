from django.views.generic import TemplateView, DetailView, ListView
from django.shortcuts import render

# Create your views here.
from core.models import Post


class PostListView(ListView):
    template_name = 'index.html'
    model = Post


class PostDetailView(DetailView):
    template_name = 'index.html'
    model = Post

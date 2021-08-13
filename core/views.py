from django.views.generic import ListView
from django.shortcuts import render, HttpResponse

# Create your views here.
from core.models import Post


class PostListView(ListView):
    template_name = 'index.html'
    model = Post
    queryset = Post.objects.order_by('-id')[:1]

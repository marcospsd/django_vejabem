from django.views.generic import ListView, DetailView, FormView
from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
import django_filters

# Create your views here.
from core.models import Post


class PostListView(ListView):
    template_name = 'index.html'
    model = Post
    queryset = Post.objects.order_by('-id')[:1]


class HistoricoListView(ListView):
    template_name = 'historico.html'
    model = Post


def post(request, post_id):
    post = Post.objects.get(slug=post_id)
    return render(request, 'post.html', {'post': post})


def searchpost(request):
    if request.method == "POST":
        search = request.POST['search']
        print(search)
        post = Post.objects.filter(title__icontains=search)
        print(post)
        return render(request, 'search.html', {'post': post})

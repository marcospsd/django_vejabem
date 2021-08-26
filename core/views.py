from django.views.generic import ListView, DetailView, FormView, TemplateView
from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy

# Create your views here.
from core.models import Post, Youtube


class PostListView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['post'] = Post.objects.order_by('-id')[:1]
        context['youtube'] = Youtube.objects.order_by('-id')[:1]
        return context


class BaseListView(TemplateView):
    template_name = 'base.html'
    def get_context_data(self, **kwargs):
        context = super(BaseListView, self).get_context_data(**kwargs)
        context['youtube'] = Youtube.objects.order_by('-id')[:1]
        return context


class HistoricoListView(ListView):
    template_name = 'historico.html'
    model = Post


def post(request, post_id):
    post = Post.objects.filter(slug=post_id)
    print(post)
    return render(request, 'post.html', {'post': post,})


def searchpost(request):
    if request.method == "POST":
        name_search = str(request.POST['search'])
        post = Post.objects.filter(title__icontains=name_search)
        return render(request, 'search.html', {'post': post})
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


class HistoricoListView(ListView):
    template_name = 'historico.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super(HistoricoListView, self).get_context_data(**kwargs)
        context['post'] = Post.objects.all()
        context['youtube'] = Youtube.objects.order_by('-id')[:1]
        return context


class YoutubeListView(ListView):
    template_name = 'hisvideos.html'
    model = Youtube

    def get_context_data(self, **kwargs):
        context = super(YoutubeListView, self).get_context_data(**kwargs)
        context['post'] = Youtube.objects.all()
        context['youtube'] = Youtube.objects.order_by('-id')[:1]
        return context


def post(request, post_id):
    post = Post.objects.filter(slug=post_id)
    youtube = Youtube.objects.order_by('-id')[:1]
    return render(request, 'post.html', {'post': post, 'youtube': youtube})


def videos(request, video_id):
    post = Youtube.objects.filter(slug=video_id)
    youtube = Youtube.objects.order_by('-id')[:1]
    return render(request, 'video.html', {'post': post, 'youtube': youtube})


def searchpost(request):
    if request.method == "POST":
        name_search = str(request.POST['search'])
        post = Post.objects.filter(title__icontains=name_search)
        youtube = Youtube.objects.order_by('-id')[:1]
        return render(request, 'search.html', {'post': post, 'youtube': youtube})

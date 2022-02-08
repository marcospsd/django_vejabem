from django.views.generic import ListView, DetailView, FormView, TemplateView
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.
from core.models import Post, Youtube, Enquete, Webinar, Dimaiz, TabelaPrecos, Circular


class PostListView(TemplateView):
    template_name = 'index.html'
    fields = ['option_one_count', 'option_two_count', 'option_three_count', 'option_four_count', 'total_votes']

    def post(self, request):
        enquete = Enquete.objects.get(pk=(Enquete.objects.order_by('-id')[:1]))
        if request.method == "POST":
            selected_option = request.POST['flexRadioDefault']
            if selected_option == 'option1':
                enquete.total_votes += 1
                enquete.option_one_count += 1
            elif selected_option == 'option2':
                enquete.total_votes += 1
                enquete.option_two_count += 1
            elif selected_option == 'option3':
                enquete.total_votes += 1
                enquete.option_three_count += 1
            elif selected_option == 'option4':
                enquete.total_votes += 1
                enquete.option_four_count += 1
            enquete.save()
            return HttpResponseRedirect('/')

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['post'] = Post.objects.order_by('-id')[:1]
        context['youtube'] = Youtube.objects.order_by('-id')[:1]
        context['enquete'] = Enquete.objects.order_by('-id')[:1]
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


class WebinarListView(ListView):
    template_name = 'webinar.html'
    model = Webinar

    def get_context_data(self, **kwargs):
        context = super(WebinarListView, self).get_context_data(**kwargs)
        context['webinar'] = Webinar.objects.all()
        context['youtube'] = Youtube.objects.order_by('-id')[:1]
        return context


class WebinarSlugView(TemplateView):
    template_name = 'webinar_slug.html'
    model = Webinar

    def get_context_data(self, **kwargs):
        context = super(WebinarSlugView, self).get_context_data(**kwargs)
        context['webinar'] = Webinar.objects.all()
        context['youtube'] = Youtube.objects.order_by('-id')[:1]
        return context

class DimaizView(ListView):
    template_name = 'dimaiz.html'
    model = Dimaiz

    def get_context_data(self, **kwargs):
        context = super(DimaizView, self).get_context_data(**kwargs)
        context['webinar'] = Webinar.objects.all()
        context['youtube'] = Youtube.objects.order_by('-id')[:1]
        context['post'] = Dimaiz.objects.order_by('-id')[:1]
        return context

class CircularesListView(ListView):
    template_name = 'list_circulares.html'
    model = Circular

    def get_context_data(self, **kwargs):
        context = super(CircularesListView, self).get_context_data(**kwargs)
        context['webinar'] = Webinar.objects.all()
        context['youtube'] = Youtube.objects.order_by('-id')[:1]
        context['circulares'] = Circular.objects.order_by('-id')
        return context


class TabelaLentesListView(ListView):
    template_name = 'list_tabelalentes.html'
    model =  TabelaPrecos

    def get_context_data(self, **kwargs):
        context = super(TabelaLentesListView, self).get_context_data(**kwargs)
        context['webinar'] = Webinar.objects.all()
        context['youtube'] = Youtube.objects.order_by('-id')[:1]
        context['tabelalentes'] = TabelaPrecos.objects.order_by('-id')
        return context


def post(request, post_id):
    post = Post.objects.filter(slug=post_id)
    youtube = Youtube.objects.order_by('-id')[:1]
    return render(request, 'post.html', {'post': post, 'youtube': youtube})


def videos(request, video_id):
    post = Youtube.objects.filter(slug=video_id)
    youtube = Youtube.objects.order_by('-id')[:1]
    return render(request, 'videos.html', {'post': post, 'youtube': youtube})


def searchpost(request):
    if request.method == "POST":
        name_search = str(request.POST['search'])
        post = Post.objects.filter(title__icontains=name_search)
        youtube = Youtube.objects.order_by('-id')[:1]
        return render(request, 'search.html', {'post': post, 'youtube': youtube})

def tabelapreco(request, tabelapreco_id):
    post = TabelaPrecos.objects.filter(slug=tabelapreco_id)
    youtube = Youtube.objects.order_by('-id')[:1]
    return render(request, 'tabelalentes_slug.html', {'post': post, 'youtube': youtube})

def circular(request, circular_id):
    post = Circular.objects.filter(slug=circular_id)
    youtube = Youtube.objects.order_by('-id')[:1]
    return render(request, 'circular_slug.html', {'post': post, 'youtube': youtube})
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Post


class HomePageView(ListView):
    template_name = "home.html"
    model = Post
    context_object_name = "posts"


class NewPostView(CreateView):
    model = Post
    template_name = "add_post.html"
    fields = '__all__'


class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

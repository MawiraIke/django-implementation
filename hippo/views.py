from django.views.generic import ListView
from django.views.generic.edit import CreateView

from .models import Post


class HomePageView(ListView):
    template_name = "home.html"
    model = Post
    context_object_name = "posts"


class NewPostView(CreateView):
    model = Post
    template_name = "add-post.html"
    fields = ['title', 'body']

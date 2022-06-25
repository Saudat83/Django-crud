from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import ListView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import DetailView
from django.urls import reverse_lazy
from .models import Post

# Create your views here.

class PostAppListView(ListView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = ["--all--"]
    success_url = reverse_lazy("blog:all")

class PostAppDetailView(DetailView):
    model = Post

class PostDeleteView(DeleteView):
    model = Post
    fields = ["--all--"]
    success_url = reverse_lazy("blog:all")
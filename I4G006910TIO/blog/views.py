from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import ListView

from .models import blogApp

class blogAppListView(ListView):
    model = Post

class blogCreateView(CreateView):
    model = Post
    fields = "--all--"
    success_url = reverse_lazy("blog:all")

class blogAppDetailView(DetailView):
    model = Post

class blogDeleteView(DeleteView):
    model = Post
    fields = "--all--"
    success_url = reverse_lazy("blog:all")





# Create your views here.

from django.shortcuts import render
from .models import Post
from django.views.generic import ListView
# Create your views here.
class Post_view(ListView):
    model = Post
    template_name = 'index.html'
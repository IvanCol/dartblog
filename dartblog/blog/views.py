from django.shortcuts import render
from django.views.generic import ListView

from .models import Post


class HomePage(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'home'
    extra_context = {
        'title': 'Home page'
    }

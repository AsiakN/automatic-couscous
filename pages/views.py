#from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Page
class HomePageView(ListView):
   model = Page
   template_name = 'home.html'
   context_object_name = 'all_posts_lists'
   
class DetailPageView(DetailView):
   model = Page
   template_name = 'about.html'
   
class PageCreateView(CreateView):
   model = Page
   template_name = 'new.html'
   fields = ['title', 'author', 'body']
   
class PageEditView(UpdateView):
   model = Page
   template_name = 'edit.html'
   fields = ['title', 'body']

   
# Create your views here.

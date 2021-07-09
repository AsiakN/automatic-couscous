#from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Page
class HomePageView(ListView):
   model = Page
   template_name = 'home.html'
   context_object_name = 'all_posts_lists'
   
class AboutPageView(TemplateView):
   template_name = 'about.html'
   

# Create your views here.

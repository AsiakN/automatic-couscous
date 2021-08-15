from django.shortcuts import render
from pages.models import CustomUser, CreateScribe

from django.views.generic import TemplateView
class HomePageView(TemplateView):
   model = CreateScribe
   #model = News
   template_name = 'home.html'
   context_object_name = 'all_posts_lists'
   
   
# Create your views here.

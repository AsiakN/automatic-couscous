from django.shortcuts import render
from pages.models import CustomUser, CreateScribe

from django.generic.edit.views import TemplateView
class HomePageView(ListView):
   model = CreateScribe
   #model = News
   template_name = 'home.html'
   context_object_name = 'all_posts_lists'
   
   def get_queryset(self):
        return News.objects.all()
# Create your views here.

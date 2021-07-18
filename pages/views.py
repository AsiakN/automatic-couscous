#from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import CustomUser, CreateScribe
#from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm


class HomePageView(ListView):
   model = CreateScribe
   template_name = 'home.html'
   

class ListPageView(ListView):
    model = CreateScribe
    template_name = 'list.html'
   # context_object_name = 
    context_object_name = 'all_posts_lists'
    

   
class DetailPageView(DetailView):
   model = CreateScribe
   template_name = 'about.html'
   
class PageCreateView(CreateView):
   model = CreateScribe
   template_name = 'new.html'
   fields = ['title', 'body',]
   success_url = reverse_lazy('list')
   
class PageEditView(UpdateView):
   model = CreateScribe
   template_name = 'edit.html'
   fields = ['title', 'body']
   success_url = reverse_lazy('list')

class SignUpView(CreateView):
   form_class = CustomUserCreationForm
   success_url = reverse_lazy('login')
   template_name = 'signup.html'
# Create your views here.

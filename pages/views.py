#from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import CustomUser, Researcher
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy

class HomePageView(ListView):
   model = CustomUser
   template_name = 'home.html'
   

class ListPageView(ListView):
    model = Researcher
    template_name = 'list.html'
    context_object_name = 'all_posts_lists'
   
class DetailPageView(DetailView):
   model = Researcher
   template_name = 'about.html'
   
class PageCreateView(CreateView):
   model = Researcher
   template_name = 'new.html'
   fields = ['author','title', 'body',]
   
class PageEditView(UpdateView):
   model = Researcher
   template_name = 'edit.html'
   fields = ['title', 'body']

class SignUpView(CreateView):
   form_class = CustomUserCreationForm
   success_url = reverse_lazy('login')
   template_name = 'signup.html'
# Create your views here.

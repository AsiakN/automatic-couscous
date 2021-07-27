from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import CustomUser, CreateScribe
#from django.views.generic import CreateView,
from django.urls import reverse_lazy, reverse
from .forms import CustomUserCreationForm, ScribeCreationForm
from scrapper.models import News

class HomePageView(ListView):
   #model = CreateScribe
   model = News
   template_name = 'home.html'
   context_object_name = 'articles'
   
   def get_queryset(self):
        return News.objects.all()
        
class ListPageView(ListView):
    model = CreateScribe
    template_name = 'list.html'
   # context_object_name = 
    context_object_name = 'all_posts_lists'
    paginate_by = 3; 
    

class DetailPageView(DetailView):
   model = CreateScribe
   template_name = 'about.html'
   context_object_name = 'all_posts_lists'
   #success_url = reverse_lazy('list')
   
class PageCreateView(CreateView):
   model = CreateScribe
   form_class = ScribeCreationForm
   template_name = 'new.html'
   
   def get_success_url(self):
        return reverse('list')
   
   def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        return self.render_to_response(
            self.get_context_data(form=form))
   
   def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if (form.is_valid()):
           return self.form_valid(form)
        
        else:
            return self.form_invalid(form)
            
   def form_valid(self, form):
       obj = form.save(commit=False)
       obj.author = self.request.user
       obj.save()
       return HttpResponseRedirect(self.get_success_url())
  
   def form_invalid(self, form):
       return self.render_to_response(
            self.get_context_data(form=form))
            
   #success_url = reverse_lazy('list')
   
class PageEditView(UpdateView):
   model = CreateScribe
   template_name = 'edit.html'
   fields = ['title', 'body']
   success_url = reverse_lazy('list')

class SignUpView(CreateView):
   form_class = CustomUserCreationForm
   success_url = reverse_lazy('login')
   template_name = 'signup.html'

class DeletePageView(DeleteView): 
  model = CreateScribe
  template_name = 'delete.html'
  
# Create your views here.

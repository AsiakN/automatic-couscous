from django import forms 
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser, CreateScribe
from ckeditor.fields import RichTextField

class CustomUserCreationForm(UserCreationForm):


   class Meta(UserCreationForm):
   
      model = CustomUser
      
      fields = ('username', 'email','Role',)
      
      help_texts = {
          'username': None,
          'email': None, 
      }
      
   def clean_passowrd(self):
      cd = self.cleaned_data
      
      return cd['password']

class CustomUserChangeForm(UserChangeForm):


   class Meta:
   
      model = CustomUser
      
      fields = ('username', 'email','Role',)
      
      help_texts ={
          'username': None, 
          'email': None, 
      }
      

class ScribeCreationForm(ModelForm):
   body = RichTextField()

   class Meta: 
      model = CreateScribe
      fields =  ['title', 'body', 'Interest', 'tags']
      

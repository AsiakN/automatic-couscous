from django import forms

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser, CreateScribe

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
      
      

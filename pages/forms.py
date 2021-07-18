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

class CustomUserChangeForm(UserChangeForm):


   class Meta:
   
      model = CustomUser
      
      fields = ('username', 'email','Role',)
      
      help_texts ={
          'username': None, 
          'email': None, 
      }
      
      

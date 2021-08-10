from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from pages.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
   def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.pop("autofocus", None)

   class Meta:
   
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
      

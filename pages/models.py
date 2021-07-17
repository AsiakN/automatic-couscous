from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser 
from django.contrib.auth import get_user_model 

Research_Areas = (
    ('Agriculture', 'AGRICULTURE'),
    ('Logisitics', 'LOGISTICS'),
    ('Engineering', 'ENGINEERING'),
    ('Healthcare', 'HEALTHCARE'),
 )
 
class CustomUser(AbstractUser):
   Interest = models.CharField(max_length=50, choices=Research_Areas, default='Logistics')
   title = models.CharField(max_length=250)
   body = models.TextField()
   author = models.ForeignKey('pages.CustomUser', on_delete=models.CASCADE, null=True,)
   
   def __str__(self):
     return self.title
     
   
   def get_absolute_url(self):
     return reverse('about', args=[str(self.id)])
   
  

#class Page(models.Model):
#  title = models.CharField(max_length=250)
 # author = models.ForeignKey('auth.User', on_delete=models.CASCADE,)
 # body = models.TextField()
  
 # def __str__(self):
  #   return self.title
  
  #def get_absolute_url(self):
   #  return reverse('about', args=[str(self.id)])
# Create your models here.

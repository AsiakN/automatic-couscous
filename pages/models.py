from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser 
from django.contrib.auth import get_user_model 
from taggit.managers import TaggableManager

Research_Areas = (
    ('Agriculture', 'AGRICULTURE'),
    ('Logisitics', 'LOGISTICS'),
    ('Engineering', 'ENGINEERING'),
    ('Healthcare', 'HEALTHCARE'),
 )
 
Job = (
 ('Executive', 'CEO'),
 ('Business Development', 'Business Development Specialist'),
 ('Research and Development', 'R&D'), 
 ('Technology', 'Software Engineer'),
)
 
class CustomUser(AbstractUser):
   UniqueName = models.CharField(max_length=50, default="")
   Role = models.CharField(max_length=50, choices=Job, default="")
     
  # def __str__(self):
   #  return self.UniqueName
   
   def get_absolute_url(self):
     return reverse('about', args=[str(self.id)])
   
class CreateScribe(models.Model):
   Interest = models.CharField(max_length=50, choices=Research_Areas, default="")
   title = models.CharField(max_length=250)
   body = models.TextField()
   author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True,)
   tags = TaggableManager()
   
      
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

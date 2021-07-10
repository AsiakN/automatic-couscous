from django.urls import reverse
from django.test import TestCase
from .models import Page
from django.contrib.auth import get_user_model

class PageModeTest(TestCase):
  
  def setUp(self):
     self.user = get_user_model().objects.create_user(
       username = 'testuser',
       email = 'test@email.com',
       password = 'secret'
       )
       
     self.page = Page.objects.create(
          title = 'A good title',
          body = 'Nice body content',
          author = self.user,
          )
     
  def test_page_content(self):
     page = Page.objects.get(id=1)
     expected_object_title = f'{self.page.title}'
     expected_object_body = f'{self.page.body}'
     expected_object_author = f'{self.page.author}'
     self.assertEqual(expected_object_title, "A good title")
     self.assertEqual(expected_object_body, 'Nice body content')
     self.assertEqual(expected_object_author, 'testuser')
     
class HomePageViewTest(TestCase):

   def setUp(self):
        self.user = get_user_model().objects.create_user(
       username = 'testuser',
       email = 'test@email.com',
       password = 'secret'
       )
        self.page = Page.objects.create(
          title = 'A good title',
          body = 'Nice body content',
          author = self.user,
          )
       
   def test_view_url_exists_at_proper_location(self):
       resp = self.client.get('/')
       self.assertEqual(resp.status_code, 200)
       
   def test_view_url_by_name(self): 
       resp = self.client.get(reverse('home'))
       self.assertEqual(resp.status_code,200)
       
   def test_view_uses_correct_template(self):
      resp = self.client.get(reverse('home'))
      self.assertEqual(resp.status_code,200)
      self.assertTemplateUsed(resp, 'home.html')
      
   def test_about_page_status_code(self):
       response = self.client.get('/page/1/')
       self.assertEqual(response.status_code,200)



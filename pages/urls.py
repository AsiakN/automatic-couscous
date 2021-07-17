from django.urls import path 
from .views import HomePageView, DetailPageView, ListPageView
from .views import PageCreateView, PageEditView, SignUpView
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage


urlpatterns = [
  path('', HomePageView.as_view(), name='home'),
  path('page/<int:pk>/', DetailPageView.as_view(), name='about'),
  path('page/new/', PageCreateView.as_view(), name='new'),
  path('page/<int:pk>/edit/', PageEditView.as_view(), name='edit'),
  path('signup/', SignUpView.as_view(), name='signup'),
  path('list/', ListPageView.as_view(), name='list'),
  path('favicon.ico',  RedirectView.as_view(url=staticfiles_storage.url('images/favicon.ico')))
]

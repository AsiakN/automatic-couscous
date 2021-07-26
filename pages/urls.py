from django.urls import path 
from .views import DetailPageView, ListPageView, HomePageView
from .views import PageCreateView, PageEditView, SignUpView, DeletePageView
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage


urlpatterns = [
  path('', HomePageView.as_view(), name='home'),
  path('<int:pk>/', DetailPageView.as_view(), name='about'),
  path('page/new/', PageCreateView.as_view(), name='new'),
  path('<int:pk>/edit', PageEditView.as_view(), name='edit'),
  path('signup/', SignUpView.as_view(), name='signup'),
  path('list/', ListPageView.as_view(), name='list'),
  path('favicon.ico',  RedirectView.as_view(url=staticfiles_storage.url('images/favicon.ico'))),
  path('delete/', DeletePageView.as_view(), name='delete')
]

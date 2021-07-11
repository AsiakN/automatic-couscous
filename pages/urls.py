from django.urls import path 
from .views import HomePageView, DetailPageView, PageCreateView, PageEditView

urlpatterns = [
  path('', HomePageView.as_view(), name='home'),
  path('page/<int:pk>/', DetailPageView.as_view(), name='about'),
  path('page/new/', PageCreateView.as_view(), name='new'),
  path('page/<int:pk>/edit/', PageEditView.as_view(), name='edit'),
]

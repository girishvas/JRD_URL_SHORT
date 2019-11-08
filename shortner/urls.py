from django.urls import path, include, re_path
from django.views.generic import TemplateView
from .views import *
from . import views


urlpatterns = [
	path('', views.HomePage.as_view(), name='home'),
    path('list/', views.UrlListView.as_view(), name='list'),
    path('create/', views.UrlCreateView.as_view(), name='create'),
    path('<slug:slug>/', ViewList.as_view(), name='view'),
]
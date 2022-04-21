from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='uber-ai-home'),
    path('app/', views.app, name='uber-app'),
]
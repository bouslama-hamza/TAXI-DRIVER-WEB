from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='uber-ai-home'),
    path('login/', views.login, name='uber-ai-login'),
]
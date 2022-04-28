from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='uber-ai-home'),
    path('sign_up/', views.singup, name='uberai-sign-up'),
    path('forget_password/' , views.forget_password , name = 'uberai-forget-password'),
    path('confirm_password/' , views.confirm_password , name = 'uberai-confirm_password'),
    path('about/' , views.about , name = 'uberai-about'),
    path('contact/' , views.contact , name = 'uberai-contact'),
    path('app/' , views.app , name = 'uberai-app'),
]
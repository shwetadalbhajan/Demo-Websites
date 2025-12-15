from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('programs/', views.programs, name='programs'),
    path('trainers/', views.trainers, name='trainers'),
    path('memberships/', views.memberships, name='memberships'),
    path('contact/', views.contact, name='contact'),
    path('demo/', views.demo, name='demo'),

]
from django.urls import path
from .import views

urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('contact/', views.news_contact, name='news_contact'),
    path('create', views.create, name='create')
]

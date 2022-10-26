from django.urls import path
from . import views

urlpatterns = [
  path('', views.book_list, name='book_list'),
  path('genero/', views.genre_list, name='genre_list'),
  path('autor/', views.autor_list, name='autor_list'),
  path('editorial/', views.publisher_list, name='publisher_list'),
  
]
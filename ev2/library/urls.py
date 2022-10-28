from django.urls import path
from . import views

urlpatterns = [
  path('', views.book_list, name='book_list'),
  path('book/<int:pk>/', views.book_detail, name='book_detail'),
  path('book/edit/<int:pk>/', views.book_edit, name='book_edit'),
  path('book/delete/<int:pk>/', views.book_delete, name="book_delete"),
  path('book/new/', views.book_new, name="book_new" ),
  path('genero/', views.genre_list, name='genre_list'),
  path('autor/', views.autor_list, name='autor_list'),
  path('editorial/', views.publisher_list, name='publisher_list'),
  
]
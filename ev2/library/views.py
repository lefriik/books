
from django.shortcuts import render, redirect, get_object_or_404

from .models import Book, Author, Genre, Publisher
from .forms import BookForm


def book_list(request):
  books = Book.objects.all()
  return render(request, 'library/book_list.html', {'book_list' : books})

def genre_list(request):
  generos= Genre.objects.all()
  return render(request, 'library/genre_list.html', {'genre_list' : generos})

def autor_list(request):
  autores = Author.objects.all()
  return render(request, 'library/autor_list.html', {'author_list': autores})

def publisher_list(request):
  editoriales = Publisher.objects.all()
  return render(request, 'library/publisher_list.html', {'publisher_list' : editoriales}) 
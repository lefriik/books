
from django.shortcuts import render, redirect, get_object_or_404

from .models import Book
from .forms import BookForm


def book_list(request):
  books = Book.objects.all()
  return render(request, 'library/book_list.html', {'book_list' : books})

def genre_list(request):
  return render(request, 'library/genre_list.html')

def autor_list(request):
  return render(request, 'library/autor_list.html')

def publisher_list(request):
  return render(request, 'library/publisher_list.html') 
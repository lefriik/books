
from django.shortcuts import render, redirect, get_object_or_404

from .models import Book, Author, Genre, Publisher
from .forms import BookForm


#------------------------- books ----------------------------------------

def book_list(request):
  books = Book.objects.all()
  return render(request, 'library/book_list.html', {'book_list' : books})

def book_detail(request, pk):
  book = get_object_or_404(Book, pk=pk)
  return render(request, 'library/book_detail.html', {'book': book})


def book_edit(request, pk):

  book = get_object_or_404(Book, pk=pk)

  if request.method == "POST":
    form = BookForm(request.POST, instance=book)

    if form.is_valid():
      book = form.save(commit=False)
      book.save()
      return redirect('book_detail', pk=book.pk)
  else:
    form = BookForm(instance=book)
  return render(request, 'library/book_edit.html', {'form': form})

def book_delete(request, pk):

    book = get_object_or_404(Book, pk=pk)

    if request.method=='POST':
      book.delete()
      return redirect('book_list')
      
    return render(request, 'library/book_detail.html', {'book': book})



def book_new(request):

  if request.method == "POST":
    form = BookForm(request.POST)

    if form.is_valid():
      book = form.save(commit=False)
      book.save()
      return redirect('book_detail', pk=book.pk)
  else:
    form = BookForm()
  return render(request, 'library/book_edit.html', {'form': form})






# ---------------------- Genre -----------------------------------------

def genre_list(request):
  generos= Genre.objects.all()
  return render(request, 'library/genre_list.html', {'genre_list' : generos})

def autor_list(request):
  autores = Author.objects.all()
  return render(request, 'library/autor_list.html', {'author_list': autores})

def publisher_list(request):
  editoriales = Publisher.objects.all()
  return render(request, 'library/publisher_list.html', {'publisher_list' : editoriales}) 
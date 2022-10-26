from django import forms
from .models import Genre, Author, Publisher, Book

class BookForm(forms.ModelForm):
  genre = forms.ModelChoiceField(queryset=Genre.objects.all(), empty_label="Seleccione un genero")
  author = forms.ModelChoiceField(queryset=Author.objects.all(), empty_label="Seleccione un Autor")
  publisher = forms.ModelChoiceField(queryset=Publisher.objects.all(), empty_label="Seleccione una Editorial")
  book = forms.ModelChoiceField(queryset=Book.objects.all(), empty_label="Seleccione un libro")
  class Meta:
    model = Book
    fields = ('genre', 'author', 'publisher', 'book')
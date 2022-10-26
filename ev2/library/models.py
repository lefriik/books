from django.db import models

# Create your models here.

class Genre(models.Model):
  name = models.CharField(max_length = 30, unique = True)

  def __str__(self):
    return self.name

class Author(models.Model):
  name = models.CharField(max_length = 30, unique = True)
  date_of_birth = models.DateTimeField(unique = True)

  def __str__(self):
    return self.name

class Publisher(models.Model):
  name = models.CharField(max_length = 30, unique = True)

  def __str__(self):
    return self.name

class Book(models.Model):

    name = models.CharField(max_length = 30, unique = True)
    author_fk = models.ForeignKey(Author, on_delete=models.CASCADE, null = True)
    genre_fk = models.ForeignKey(Genre, on_delete=models.CASCADE, null = True)
    publisher_fk = models.ForeignKey(Publisher, on_delete=models.CASCADE, null = True)
    





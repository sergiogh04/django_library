from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ManyToManyField(Author)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    publish_date = models.DateField()
    summary = models.TextField()
    def __str__(self):
        return self.title


class User(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=16)
    def __str__(self):
        return self.username

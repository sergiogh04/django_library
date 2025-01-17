from django.contrib import admin

import books
from books.models import Author, Book, Genre

# Register your models here.


admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
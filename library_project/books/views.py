from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.template import loader

from books.models import Book, Author, Genre


# Create your views herd
def index(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'books/index.html', context)

def booksDetails(request, book_id):
    book = Book.objects.get(pk=book_id)
    context = {'book': book}
    return render(request, 'books/booksDetails.html', context)

def authorDetail(request, author_id):
    author = Author.objects.get(pk=author_id)
    context = {'author': author}
    return render(request, 'books/authorsDetails.html', context)

def authorList(request):
    authors = Author.objects.all()
    context = {'authors': authors}
    return render(request, 'books/authorsDetails.html', context)




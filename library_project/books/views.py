from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.shortcuts import render
from django.template import loader
from django.urls import reverse

from books.models import Book, Author, Genre


# Create your views herd
def index(request):
    books = Book.objects.all()
    author = Author.objects.all()
    context = {'books': books, 'author': author}
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
    return render(request, 'books/authorList.html', context)


def addAuthors(request):


    if request.method == 'POST':
        name = request.POST.get('name')
        last_name = request.POST.get('last_name')
        birth_date = request.POST.get('birth_date')

        Author.objects.create(name=name, last_name=last_name, birth_date=birth_date)

        return redirect('books:author_list')

    return render(request, 'books/addAuthors.html')


def genreList(request):
    genres = Genre.objects.all()
    context = {'genres': genres}
    return render(request, 'books/genreList.html',context)
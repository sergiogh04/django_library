from django.urls import path

from . import views
from .views import authorList


app_name = "books"

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),

    path('authors/', views.authorList, name='author_list'),

    path('authors/<int:author_id>/', views.authorDetail, name='author_detail'),

    path('<int:book_id>/', views.booksDetails, name='booksDetails'),

    path("addAuthors", views.addAuthors, name="addAuthors"),

    path("genreList", views.genreList, name="genreList"),

    ]

    # ex: /polls/5/

from django.test import TestCase, Client
from django.urls import reverse
from books.models import Author, Book, Genre

class LibraryTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.author = Author.objects.create(name="Brandon", last_name="Sanderson")
        self.genre = Genre.objects.create(name="Fantasy")
        self.book = Book.objects.create(title="El archivo de las tormentas", genre=self.genre, publish_date="2001-04-08", summary="Brandon Sanderson (Lincoln, Nebraska, 19 de diciembre de 1975) es un escritor estadounidense de literatura fantástica y ciencia ficción. Es conocido sobre todo por el universo ficticio de Cosmere, en el que se ambientan la mayoría de sus novelas de fantasía, entre las que destacan las series Nacidos de la bruma (Mistborn) y El archivo de las tormentas. Fuera del Cosmere, ha escrito varias series juveniles y para jóvenes adultos, como The Reckoners, la serie Skyward y la serie Alcatraz. También es conocido por haber terminado la serie de alta fantasía de Robert Jordan La Rueda del Tiempo. Sanderson ha creado varias novelas gráficas de fantasía, como White Sand o Dark One.")
        self.book.author.add(self.author)

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "El archivo de las tormentas")

    def test_book_detail_view(self):
        response = self.client.get(reverse('book_detail', args=[self.book.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Brandon Sanderson")

    def test_author_list_view(self):
        response = self.client.get(reverse('author_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Brandon Sanderson")


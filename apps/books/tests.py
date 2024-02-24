from django.test import TestCase
from django.urls import reverse
from apps.books.models import Book, BookGenre, BookAuthor

class TestBooks(TestCase):
    def setUp(self):
        author = BookAuthor.objects.create(
            first_name = 'first_name1',
            last_name = 'last_name1',
            birthdate = '2024-10-23',
            website = 'https://djmolles.com',
            about = 'about1'
        )
        self.author = author
        genre = BookGenre.objects.create(
            name = 'ganre-1'
        )
        self.genre = genre
        print(self.genre)

        # book = Book.objects.create(
        #     title = 'book1',
        #     slug = '11183081212037982',
        #     description = 'description1',
        #     isbn = '0001987987729',
        #     language = 'en',
        #     page = '143',
        #     # genre = self.genre,
        #     # authors = self.author

        # )
        # self.book = book

    def testBooksUrls(self):    

        response1 = self.client.get(reverse('books:home'))
        response2 = self.client.get(reverse('books:book-list'))
        # response3 = self.client.get(reverse('books:book-detail'))
        # response4 = self.client.get(reverse('books:book-genre'))
        # response5 = self.client.get(reverse('books:book-author'))
        response6 = self.client.get(reverse('books:book-authors'))
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(response2.status_code, 200)
        # self.assertEqual(response3.status_code, 200)
        # self.assertEqual(response4.status_code, 200)
        # self.assertEqual(response5.status_code, 200)
        self.assertEqual(response6.status_code, 200)

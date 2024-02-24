from django.urls import path
from .views import *

app_name = 'books'
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('books/', BookListView.as_view(), name='book-list'),
    path('book-Detail/<slug:slug>', BookDetailView.as_view(), name='book-detail'),
    path('book-Detail-create/<int:id>', CreateReviewView.as_view(), name='create-review'),
    path('book-Detail-update/<int:id>', UpdateReviewView.as_view(), name='update-review'),
    path('book-Detail-delete/<int:id>', DeleteReviewView.as_view(), name='delete-review'),
    path('book-Genre/<int:id>', BookGenreView.as_view(), name='book-genre'),
    path('book-Author-detail/<int:id>', BookAuthorDetailView.as_view(), name='book-author'),
    path('book-Authors/', BookAuthorListView.as_view(), name='book-authors'),
    path('book-Add-Author/', AddAuthorView.as_view(), name='add-author'),
    path('book-Add-Book/', AddBookView.as_view(), name='add-book'),
]
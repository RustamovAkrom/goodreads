from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.shared.models import AbstractBaseModel
from apps.books.models import Book

class User(AbstractUser):
    avatar = models.ImageField(upload_to='users/avatar/', null=True, default='default/user_img/user.png')
    middle_name = models.CharField(max_length=130)


class BookShelf(AbstractBaseModel):
    name = models.CharField(max_length=130)
    user = models.ForeignKey(User, models.CASCADE, 'bookshelf')
    books = models.ManyToManyField(Book, "bookshelves")
from django.db import models
from apps.shared.models import AbstractBaseModel
from django.core.validators import MaxValueValidator, MinValueValidator
from django.template.defaultfilters import slugify
import random

class LanguageChoices(models.TextChoices):
    ENGLISH = 'en', "English"
    FRANCE = 'fr', "France"
    RUSSIAN = 'ru', 'Russian'
    ARABIC = 'ab', 'Arabic'
    UZBEK = 'uz', 'Uzbek'


class BookGenre(AbstractBaseModel):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class BookAuthor(AbstractBaseModel):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    birthdate = models.DateField()
    website = models.URLField()
    avatar = models.ImageField(upload_to='authors/avatar', null=True, default='default/author_img/author.png')
    about = models.TextField()
    email = models.EmailField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(AbstractBaseModel):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    published = models.DateField()
    isbn = models.CharField(max_length=120)
    language = models.CharField(max_length=7, choices=LanguageChoices.choices, default=LanguageChoices.ENGLISH)
    page = models.IntegerField()
    cover = models.ImageField(upload_to="books/cover", null=True, default='default/book_img/book.png')
    genre = models.ManyToManyField(BookGenre, "books")
    authors = models.ManyToManyField(BookAuthor, "books")

    def __str__(self):
        return self.title

class BookReview(AbstractBaseModel):
    book = models.ForeignKey("books.Book", models.CASCADE, "reviews")
    user = models.ForeignKey("users.User", models.CASCADE, "reviews")
    body = models.TextField()
    rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    like_count = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.user} --> {self.book}"
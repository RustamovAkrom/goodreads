from django.contrib import admin
from .models import (
                    BookGenre, 
                    BookAuthor,
                    Book, 
                    BookReview,
                    )


admin.site.register(BookGenre)
admin.site.register(BookAuthor)
admin.site.register(Book)
admin.site.register(BookReview)
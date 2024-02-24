from django import forms
from apps.books.models import BookReview, BookAuthor, Book
from apps.books.models import LanguageChoices
from django.template.defaultfilters import slugify

class CreateReviewForm(forms.ModelForm):
    rating = forms.IntegerField(min_value=1, max_value=5)
    body = forms.Textarea()

    class Meta:
        model = BookReview
        fields = ('body', 'rating', 'like_count')
        


    
class AddBookAuthorForm(forms.ModelForm):
    class Meta:
        model = BookAuthor
        fields = ('first_name', 
                  'last_name', 
                  'birthdate', 
                  'website', 
                  'avatar', 
                  'about')

class AddBookForm(forms.ModelForm):
    title = forms.CharField()
    descriptions = forms.Textarea()
    published = forms.DateField()
    isbn = forms.IntegerField()
    language = forms.ChoiceField(choices=LanguageChoices)
    page = forms.IntegerField()
    cover = forms.FileField()
    class Meta:
        model = Book
        fields = ('title',
                  'slug',
                  'description', 
                  'published',
                  'isbn', 
                  'language', 
                  'page',
                  'cover',
                  'genre', 
                  'authors')
        widgets = {
            "title":forms.TextInput(attrs={"placeholder":"book title"}),
            "description":forms.Textarea(attrs={"placeholder":"book description"}),
            "published":forms.DateInput(attrs={"placeholder":"book published date"}),
            "isbn":forms.NumberInput(attrs={"placeholder":"book isbn"}),
            "page":forms.NumberInput(attrs={"placeholder":"book page"}),
            "cover":forms.FileInput(attrs={"placeholder":"book image"}),
        }

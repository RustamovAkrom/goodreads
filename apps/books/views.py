from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, TemplateView, CreateView
from django.views import View
from apps.users.models import User
from apps.books.models import Book, BookGenre, BookReview, BookAuthor
from .forms import CreateReviewForm, AddBookAuthorForm, AddBookForm
from django.urls import reverse, reverse_lazy
from django.core.paginator import Paginator
from django.contrib import messages



class HomePageView(View):
    def get(self, request):
        books = Book.objects.all()
        recomendet_books = books.order_by('id')[:4]
        return render(request, "home.html", {
            "recomendet_books":recomendet_books,
            "corusel_books":books.order_by('created_at'),
            # "videos":...,
            "featured_books":...
        })
    

class BookListView(View):
    def get(self, request):
        books = Book.objects.all()

        page = request.GET.get('page', 1)
        size = request.GET.get('size', 3)
        paginator = Paginator(books.order_by('id'), size)
        page_obj = paginator.page(page)
        return render(request, 'books/book_list.html', {
            "page_obj":page_obj, 
            "corusel_books":books.order_by('-created_at')
        })


class BookDetailView(View):
    def get(self, request, slug):
        book = Book.objects.get(slug=slug)
        form = CreateReviewForm()
        return render(request, "books/book_detail.html", 
                      {
                          "book":book,
                          "form":form,
                          "count_reated":"4.0",
                          "count_reviews":"34",
                          "count_likes":"233"
                      })


class CreateReviewView(View):

    def post(self, request, id):
        book = Book.objects.get(id=id)
        user = User.objects.get(username=request.user.username)

        form = CreateReviewForm(request.POST)

        if form.is_valid():
            BookReview.objects.create(
                user = user,
                book = book,
                body = form.cleaned_data.get("body"),
                rating = form.cleaned_data.get("rating")
            )
            messages.success(request, "Creating new review")
            return redirect(reverse("books:book-detail", kwargs={"slug":book.slug}))
        else:
            messages.warning(request, "Your review is not valid !")
            context = {
                "book":book,
                "form":form
            }
        return render(request, "books/book_detial.html", context=context)

class UpdateReviewView(View):
    def get(self, request, id):
        reviews = get_object_or_404(BookReview, id=id)
        form = CreateReviewForm(request.POST, instance=reviews)
        return render(request, "books/update_review.html", {"form":form})
    
    def post(self, request, id):
        review = BookReview.objects.get(id=id)
        form = CreateReviewForm(request.POST, instance=review)
        if form.is_valid():
            messages.success(request, "Review succesffuly updated")
            form.save()
            return redirect(reverse("books:book-detail", kwargs={"slug":review.book.slug}))
        messages.warning(request, "your updating review is not valid")
        return render(request, reverse("books:book-detail", kwargs={"slug":review.book.slug}), {"form":form})
        

class DeleteReviewView(View):
    def get(self, request, id):
        review = get_object_or_404(BookReview, id=id)
        return render(request, "books/delete_review.html", {"review":review})
    
    def post(self, request, id):
        review = get_object_or_404(BookReview, id=id)
        messages.success(request, "Review succesffully deleted")
        review.delete()
        return render(request, reverse("books:book-detail", kwargs={"slug":review.book.slug}), {"review":review})



class BookGenreView(View):
    def get(self, request, id):
        genre = BookGenre.objects.get(id=id)
        books = Book.objects.filter(genre=genre)
        # print(genre)
        return render(request, "books/book_list.html", {
            "page_obj":books
        })


class BookAuthorListView(ListView):
    model = BookAuthor
    template_name = 'books/author_list.html'
    context_object_name = 'authors'

class BookAuthorDetailView(View):
    def get(self, request, id):
        author = BookAuthor.objects.get(id=id)
        return render(request, "books/book_authors_detail.html", {
            "author":author,
        })
    

class AddAuthorView(CreateView):
    form_class = AddBookAuthorForm
    template_name = 'books/add_author.html'
    context_object_name = 'form'
    success_url = reverse_lazy('books:home')
    
    # def get(self, request):
    #     form = AddBookAuthorForm()
    #     return render(request, "books/add_author.html", {"form":form})
    
    # def post(self, request):
    #     form = AddBookAuthorForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('books:home')
    #     return render(request, 'books/add_author.html')

class AddBookView(CreateView):
    form_class = AddBookForm
    template_name = 'books/add_book.html'
    context_object_name = 'form'
    success_url = reverse_lazy('books:home')
    # def get(self, request):
    #     form = AddBookForm()
    #     return render(request, "books/add_book.html", {"form":form})

    # def post(self, request):
    #     form = AddBookForm(request.POST)
    #     if form.is_valid():
    #         Book.objects.create(
    #             slug  =  slugify(form.cleaned_data.get('title')),
    #         )
    #     return render(request, "books/add_book.html")

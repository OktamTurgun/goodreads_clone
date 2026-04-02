from django.shortcuts import get_object_or_404, render
from django.views import View
from .models import Book

    
def home_view(request):
    books = Book.objects.prefetch_related('authors').all()
    return render(request, 'books/home.html', {'books': books})

def book_detail_view(request, pk):
    book    = get_object_or_404(Book.objects.prefetch_related('authors'), pk=pk)
    reviews = book.reviews.select_related('user').all()
    return render(request, 'books/detail.html', {
        'book':    book,
        'reviews': reviews,
    })

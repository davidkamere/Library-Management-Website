from django.shortcuts import render
from .models import Book
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    """ view for the Landing page"""
    all_books = Book.objects.order_by('book_name')
    paginator = Paginator(all_books, 10)
    page = request.GET.get('page')
    books = paginator.get_page(page)
    context = {'books': books}
    return render(request, 'the_collection/index.html', context)


def book_details(request):
    return render(request, 'the_collection/book_details.html')
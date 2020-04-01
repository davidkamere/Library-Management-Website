from django.shortcuts import render
from .models import Borrowed, Book
from .forms import BorrowForm


# Create your views here.
def user_dashboard(request):

    if request.method == 'POST':
        form = BorrowForm(data=request.POST)
        if form.is_valid():
            book_name = request.POST.get('book_name')
            book = Book(id=book_name)
            borrowed_by = request.user
            new_borrow = Borrowed.objects.create(book=book, borrowed_by=borrowed_by)
            new_borrow.save()
            
    borrowed_books = Borrowed.objects.filter(borrowed_by=request.user).order_by('-due_date')

    return render(request, 'dashboards/user_dashboards.html', {'books': borrowed_books})


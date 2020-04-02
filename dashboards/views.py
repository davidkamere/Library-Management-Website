from django.shortcuts import render
from .models import Borrowed, Book, Waiting
from .forms import BorrowForm, WaitingForm


# Create your views here.
def user_dashboard(request):

    if request.method == 'POST':
        if "reserve" in request.POST:
            form = BorrowForm(data=request.POST)
            if form.is_valid():
                book_name = request.POST.get('book_name')
                book = Book.objects.get(id=book_name)
                book.book_status = 3
                book.save()
                borrowed_by = request.user
                new_borrow = Borrowed.objects.create(book=book, borrowed_by=borrowed_by)
                new_borrow.save()

        elif "waiting" in request.POST:
            form = WaitingForm(data=request.POST)
            if form.is_valid():
                book_name = request.POST.get('book_name2')
                book = Book.objects.get(id=book_name)
                waiting_user = request.user
                new_waiting = Waiting.objects.create(book=book, user=waiting_user)
                new_waiting.save()
            
    borrowed_books = Borrowed.objects.filter(borrowed_by=request.user).order_by('-due_date')
    books_in_waiting = Waiting.objects.filter(user=request.user)

    return render(request,
                  'dashboards/user_dashboards.html',
                  {'books': borrowed_books, 'waiting': books_in_waiting})


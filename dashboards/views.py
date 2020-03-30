from django.shortcuts import render
from .models import Borrowed


# Create your views here.
def user_dashboard(request):
    borrowed_books = Borrowed.objects.filter(borrowed_by=request.user).order_by('-due_date')

    return render(request, 'dashboards/user_dashboards.html', {'books': borrowed_books})


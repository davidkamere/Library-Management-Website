from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from the_collection.models import Book


# Create your views here.
def index(request):
    """ view for the Landing page"""
    all_books = Book.objects.order_by('book_name')
    paginator = Paginator(all_books, 10)
    page = request.GET.get('page')
    books = paginator.get_page(page)
    context = {'books': books}
    return render(request, 'the_collection/index.html', context)


def search_posts(request):
    if request.method == 'GET':
        query = request.GET.get('q')

        submitbutton = request.GET.get('submit')

        if query is not None:
            # filters
            results = Book.objects.filter(Q(publisher__name__contains=query) |
                                          Q(author__name__contains=query) |
                                          Q(book_name__contains=query) |
                                          Q(subject__contains=query)).distinct()

            context = {'results': results,
                       'submitbutton': submitbutton}

            return render(request, 'the_collection/search.html', context)

        else:
            return render(request, 'the_collection/index.html')

    else:
        return render(request, 'the_collection/index.html')


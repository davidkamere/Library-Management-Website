from django.contrib import admin
from the_collection.models import Book, Author, Publisher


# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publisher)
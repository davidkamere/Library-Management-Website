from django.db import models
from the_collection.models import Book
from django.contrib.auth.models import User


# Create your models here
class Waiting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Borrowed(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book', blank=True, null=True)
    due_date = models.DateTimeField(blank=True, null=True)
    borrowed_by = models.ManyToManyField(User)
    last_borrowed_on = models.DateTimeField()
    waiting_users = models.ForeignKey(Waiting,
                                      on_delete=models.CASCADE,
                                      related_name='waiting_user',
                                      blank=True, null=True)

    def __str__(self):
        return "%s" % self.book.book_name

    class Meta:
        verbose_name_plural = 'Books borrowed'
        ordering = ['-due_date']



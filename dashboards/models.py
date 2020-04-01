from django.db import models
from the_collection.models import Book
from django.contrib.auth.models import User
from datetime import datetime, timedelta


# Create your models here
def get_due_date():
    return datetime.today() + timedelta(days=60)


class Waiting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Borrowed(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE, blank=True, null=True)
    due_date = models.DateTimeField(default=get_due_date, blank=True, null=True)
    borrowed_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', blank=True, null=True)
    borrowed_on = models.DateTimeField(auto_now_add=True, blank=True)
    waiting_users = models.ForeignKey(Waiting,
                                      on_delete=models.CASCADE,
                                      related_name='waiting_user',
                                      blank=True, null=True)

    def __str__(self):
        return "%s" % self.book.book_name

    class Meta:
        verbose_name_plural = 'Books borrowed'
        ordering = ['-due_date']



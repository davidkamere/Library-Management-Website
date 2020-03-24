from django.db import models


# Create your models here.
# Author has many to one relationship
class Author(models.Model):
    name = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name_plural = 'Authors'


# Author has many to one relationship
class Publisher(models.Model):
    name = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name_plural = 'Publishers'


# Main book entity
class Book(models.Model):
    # field options
    FORMAT_CHOICES = (
        (1, "Hardcover"),
        (2, "Paperback"),
        (3, "Audio-book"),
        (4, "E-book"),
        (5, "Newspaper"),
        (6, "Magazine"),
        (7, "Journal"),
    )

    STATUS_CHOICES = (
        (1, "Available"),
        (2, "Reserved"),
        (3, "Borrowed"),
    )

    book_name = models.CharField(max_length=500, blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author', blank=True, null=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name='publisher', blank=True, null=True)
    ISBN = models.IntegerField()
    subject = models.CharField(max_length=200, blank=True, null=True)
    language = models.CharField(max_length=200, blank=True, null=True)
    number_of_pages = models.IntegerField()
    book_format = models.IntegerField(choices=FORMAT_CHOICES, default=1)
    book_status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    copies_available = models.IntegerField()
    cover = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return "%s" % self.book_name

    class Meta:
        verbose_name_plural = 'Books'





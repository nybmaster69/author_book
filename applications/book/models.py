from django.db import models

from applications.author.models import Author


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author')
    title = models.CharField(max_length=255)
    date_of_publish = models.DateTimeField(default=1900)
    picture = models.ImageField(upload_to='media')

    is_bestseller = models.BooleanField(True)

    def __str__(self):
        return f'{self.author.name} -> {self.title}'

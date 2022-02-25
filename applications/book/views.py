from rest_framework import generics

from applications.book.models import Book
from applications.book.serializers import BookSerializer


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

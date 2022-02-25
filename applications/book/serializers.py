from rest_framework import serializers

from applications.book.models import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('author', 'title')

from rest_framework import generics

from applications.author.models import Author
from applications.author.serializers import AuthorSerializer


class AuthorListView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


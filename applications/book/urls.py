from django.urls import path, include

from applications.book.views import BookListView

urlpatterns = [
    path('book/', BookListView.as_view()),
]

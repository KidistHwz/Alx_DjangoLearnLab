# api/views.py

from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()  # All books in the database
    serializer_class = BookSerializer  # Use the BookSerializer to convert data to/from JSON

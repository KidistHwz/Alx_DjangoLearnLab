# api/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

# Set up the router
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Other routes can be added here if needed, for example, for individual views
    path('', include(router.urls)),  # This includes all routes registered with the router
]

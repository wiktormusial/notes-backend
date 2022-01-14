from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Note, Category
from .serializers import NoteSerializer, CategorySerializer
# Create your views here.

class NotesViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    # permission_classes = [IsAuthenticated]
    serializer_class = NoteSerializer

    def get_queryset(self, *args, **kwargs):
        author = self.request.user.id
        notes = Note.objects.all().filter(author=author)

        return notes

class CategoriesViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    # permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer

    def get_queryset(self, *args, **kwargs):
        author = self.request.user.id
        categories = Category.objects.all().filter(author=author)

        return categories

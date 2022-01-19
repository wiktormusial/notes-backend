from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Note, Category
from .serializers import NoteSerializer, CategorySerializer


class NotesViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    # permission_classes = [IsAuthenticated]
    serializer_class = NoteSerializer

    def get_queryset(self, *args, **kwargs):
        author = self.request.user.id
        queryset = Note.objects.all().filter(author=author)

        is_archived = self.request.query_params.get('is_archived')

        if is_archived is not None:
            queryset = queryset.filter(is_archived=is_archived)

        return queryset


class CategoriesViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    # permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer

    def get_queryset(self, *args, **kwargs):
        author = self.request.user.id
        categories = Category.objects.all().filter(author=author)

        return categories

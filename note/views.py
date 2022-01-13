from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

from .models import Note, Category
from .serializers import NoteSerializer
# Create your views here.

class NotesViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = NoteSerializer

    def get_queryset(self, **kwargs):
        token = self.kwargs['token']
        author = Token.objects.get(key=token).user_id
        notes = Note.objects.all().filter(author=author)

        return notes

class CategoriesViewSet():
    pass

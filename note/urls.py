from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import NotesViewSet, CategoriesViewSet

urlpatterns = [
    path('<str:token>', NotesViewSet.as_view({'get': 'list', 'post': 'create'}), name="notesallview"),
    path('<str:token>/<int:pk>', NotesViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}, name="noteseditview"))
]

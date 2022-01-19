from django.urls import path

from .views import NotesViewSet, CategoriesViewSet


urlpatterns = [
    path('notes',
         NotesViewSet.as_view({'get': 'list',
                              'post': 'create'}),
         name="notes"),
    path('notes/<int:pk>',
         NotesViewSet.as_view({'get': 'retrieve',
                               'put': 'update',
                               'delete': 'destroy'}),
         name="notes"),
    path('categories',
         CategoriesViewSet.as_view({'get': 'list',
                                    'post': 'create'}),
         name="categories"),
    path('categories/<int:pk>',
         CategoriesViewSet.as_view({'get': 'retrieve',
                                    'put': 'update',
                                    'delete': 'destroy'}),
         name="categories")
]

from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import NotesViewSet, CategoriesViewSet

router = SimpleRouter()
router.register('<str:token>/', NotesViewSet, basename="notes")
router.register('<str:token>/categories/', CategoriesViewSet, basename="categories")

urlpatterns = router.urls

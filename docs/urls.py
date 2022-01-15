from django.urls import path

from .views import SchemaView

urlpatterns = [
    path('', SchemaView.as_view(), name='docs')
]

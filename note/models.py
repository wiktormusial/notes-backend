import uuid

from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

from utils.models import TimeStampedModel

# Create your models here.
class Note(TimeStampedModel):
    slug = models.SlugField(blank=True)
    title = models.CharField(max_length=150)
    body = models.TextField()
    category = models.ForeignKey(
        'Category',
        on_delete = models.CASCADE,
    )
    author = models.ForeignKey(
        User,
        on_delete = models.CASCADE
    )
    is_archived = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(f'{uuid.uuid4()}-{self.title}')
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Note"
        verbose_name_plural = "Notes"

class Category(TimeStampedModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    author = models.ForeignKey(
        User,
        related_name = "categories",
        on_delete = models.CASCADE
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

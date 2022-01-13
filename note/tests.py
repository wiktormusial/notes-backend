from django.test import TestCase
from django.contrib.auth.models import User

from .models import Note, Category

#models
class NoteTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="test_user", password="pass")
        user = User.objects.get(username="test_user")

        Category.objects.create(name="test title", author=user)
        category = Category.objects.get(name="test title")

        Note.objects.create(title="Test title", body="test body", category=category, author=user)

    def test_notes_shows_names(self):
        note = Note.objects.get(title="Test title")
        self.assertEqual(note.__str__(), "Test title")

    def test_note_is_archived(self):
        note = Note.objects.get(title="Test title")
        self.assertEqual(note.is_archived, False)

    def test_author_name(self):
        note = Note.objects.get(title="Test title")
        self.assertEqual(note.author.username, "test_user")


class CategoryTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="test_user", password="pass")
        user = User.objects.get(username="test_user")

        Category.objects.create(name="test title", author=user)

    def test_categories_have_names(self):
        category = Category.objects.get(name="test title")
        self.assertEqual(category.__str__(), "test title")

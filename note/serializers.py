from rest_framework import serializers

from .models import Note, Category

class NoteSerializer(serializers.ModelSerializer):
    slug = serializers.CharField(max_length=100, read_only=True)

    class Meta:
        model = Note
        fields = ['id', 'slug', 'created_at', 'update_at', 'title', 'body', 'is_archived', 'author', 'category']
        read_only_fields = ('author', 'slug', )

    def create(self, validated_data):
        note = Note(**validated_data)
        note.author = self.context['request'].user
        note.save()

        return note

    def validate_category(self, value):
        if not self.context['request'].user.categories.filter(pk=value.pk).exists():
            raise serializers.ValidationError('invalid category')
        return value

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'created_at', 'update_at', 'slug', 'author', 'name', 'description']
        read_only_fields = ('author', 'slug')


    def create(self, validated_data):
        category = Category(**validated_data)
        category.author = self.context['request'].user
        category.save()

        return category

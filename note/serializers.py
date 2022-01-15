from rest_framework import serializers

from .models import Note, Category

class NoteSerializer(serializers.ModelSerializer):
    slug = serializers.CharField(max_length=100, read_only=True)

    class Meta:
        model = Note
        fields = "__all__"

    def create(self, validated_data):
        obj = Note.objects.create(**validated_data)
        obj.author = self.context['request'].user
        obj.save()

        return obj

    def validate_category(self, value):
        if not self.context['request'].user.categories.filter(pk=value.pk).exists():
            raise serializers.ValidationError('invalid category')
        return value

    def validate_author(self, value):
        if not self.context['request'].user.id == value.id:
            raise serializers.ValidationError('invalid author')
        return value

class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.CharField(max_length=100, read_only=True)

    class Meta:
        model = Category
        fields = "__all__"

    def create(self, validated_data):
        obj = Category.objects.create(**validated_data)
        obj.author = self.context['request'].user
        obj.save()

        return obj

    def validate_author(self, value):
        if not self.context['request'].user.id == value.id:
            raise serializers.ValidationError('invalid author')
        return value

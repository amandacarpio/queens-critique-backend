from .models import Comment
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'name', 'city', 'rating', 'review']
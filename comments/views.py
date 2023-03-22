from django.shortcuts import render
from .models import Comment
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import CommentSerializer

# Create your views here.
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.AllowAny]
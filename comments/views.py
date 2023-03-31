from django.shortcuts import render
from .models import Comment
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import CommentSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.AllowAny]
    
    @action(methods=['GET'], detail=True)
    def restaurant_comments(self, request, pk=None):
        queryset = Comment.objects.filter(yelpId = pk)
        serializer = self.get_serializer(queryset, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response([], status=status.HTTP_200_OK)    

    @action(methods=['GET', 'PUT'], detail=True)
    def individual_review(self, request, pk=None):
        if(request.method == 'PUT'): 
            return Response([request.payload], status=status.HTTP_200_OK)  
        queryset = Comment.objects.filter(id = pk)
        serializer = self.get_serializer(queryset, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response([], status=status.HTTP_200_OK)
    
    # @action(methods=['PUT'], detail=True)
    # def individual_review(self, request, pk=None):
    #     queryset = Comment.objects.filter(id = pk)
    #     serializer = self.get_serializer(queryset, many=True)
    #     if serializer.data:
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response([], status=status.HTTP_200_OK)
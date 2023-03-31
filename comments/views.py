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

    @action(methods=['GET'], detail=True)
    def individual_review(self, request, pk=None):
        queryset = Comment.objects.filter(id = pk)
        serializer = self.get_serializer(queryset, many=True)
        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response([], status=status.HTTP_200_OK)
    
    @action(methods=['POST'], detail=True)
    def individual_review(self, request, pk=None):
        print(self.get_object())
        instance=self.get_object()
        data={
            "name": request.data.get("name"),
            "city": request.data.get("city"),
            "rating": request.data.get("rating"),
            "review": request.data.get("review"),
            "yelpId": request.data.get("yelpId")
        }
        serializer = self.serializer_class(instance=instance,
            data=data, # or request.data
            partial=True)
        # queryset = Comment.objects.filter(id = pk)
        # serializer = self.get_serializer(queryset)
        # if serializer.data:
        #     return Response(serializer.data, status=status.HTTP_200_OK)
        # return Response([], status=status.HTTP_200_OK)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
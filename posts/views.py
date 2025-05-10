from django.shortcuts import render
from  rest_framework import generics,permissions
from .serializers import PostSerializers,VoteSerializers
from .models import Post,Vote

# Create your views here.

class PostList(generics.ListCreateAPIView):
    queryset= Post.objects.all()
    serializer_class= PostSerializers
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(authour=self.request.user)

class VoteCreate(generics.CreateAPIView):
    queryset= Vote.objects.all()
    serializer_class= VoteSerializers
    permission_classes=[permissions.IsAuthenticated]
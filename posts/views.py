from django.shortcuts import render
from  rest_framework import generics,permissions,mixins,status
from .serializers import PostSerializers,VoteSerializers
from rest_framework.exceptions import ValidationError 
from rest_framework.response import Response
from .models import Post,Vote

# Create your views here.

class PostList(generics.ListCreateAPIView):
    queryset= Post.objects.all()
    serializer_class= PostSerializers
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(authour=self.request.user)


class VoteCreate(generics.CreateAPIView,mixins.DestroyModelMixin):
    serializer_class= VoteSerializers
    permission_classes=[permissions.IsAuthenticated]

    def get_queryset(self):
        user= self.request.user
        post= Post.objects.get(pk=self.kwargs['pk'])
        return Vote.objects.filter(voter=user, post=post)
    
    def perform_create(self, serializer):
        if self.get_queryset().exists():
            raise ValidationError('you have already voted for this post!')
        serializer.save(voter=self.request.user, post=Post.objects.get(pk=self.kwargs['pk']))
                            
    def delete(self,request,*args,**kwargs):     
        if self.get_queryset().exists():
            self.get_queryset().delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise ValidationError("you have not vote for this post before ")

    
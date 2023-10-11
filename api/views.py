from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from api.models import Todo
from rest_framework import permissions, filters
from api.serializers import TodoSerializers
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class TodoAPIView(ListCreateAPIView):
    serializer_class = TodoSerializers
    permission_classes = (IsAuthenticated,)
    filter_backends=[DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['id', 'title', 'completed']
    search_fields = ['id', 'title', 'completed']
    ordering_fields = ['id', 'title', 'completed']

    

    ## Set owner to the login user
    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    
    ## Filter by logged in user. 
    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)
    


class TodoDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializers
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

  
    ## Filter by logged in user. 
    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)

     



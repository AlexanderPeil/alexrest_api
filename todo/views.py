from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .models import Todo
from .serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Todo.objects.all().order_by('-ctreated_at')
    serializer_class = TodoSerializer
    permission_classes = [] # permissions.IsAuthenticated

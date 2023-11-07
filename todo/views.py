from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer
from django.core import serializers
from django.http import HttpResponse


class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Todo.objects.all().order_by('-ctreated_at')
    serializer_class = TodoSerializer
    permission_classes = [] # permissions.IsAuthenticated

    def create(self, request):
        title = request.data.get('title')
        description = request.data.get('description')        

        if title and description:
            todo = Todo.objects.create(
                title=title,
                description=description,
                user=request.user
            )

        serializer = TodoSerializer(todo)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

        # serialized_obj = serializers.serialize('json', [todo])
        # return HttpResponse(serialized_obj, content_type='application/json')
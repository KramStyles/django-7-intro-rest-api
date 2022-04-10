from functools import partial
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.reverse import reverse

from languages import serializers

from .models import Tasks
from .serializers import TodoSerializer

class TodoList(APIView):
    def get(self, request):
        todo = Tasks.objects.all()
        todo_data = TodoSerializer(todo, many=True)
        return Response(todo_data.data)

    def post(self, request):
        todo = TodoSerializer(data=request.data)
        if todo.is_valid(): 
            item = todo.save()
            item.finished = False
            item.url = reverse('todo-single', args=[item.id], request=request)
            item.save()
        return Response(todo.data)

    def delete(self, request):
        Tasks.objects.all().delete()
        return Response(None)

class TodoView(ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TodoSerializer


class TodoSingle(APIView):
    def get(self, request, pk):
        todo = Tasks.objects.get(pk=pk)

        serializer = TodoSerializer(todo)
        return Response(serializer.data)

    # To edit a todo list
    def patch(self, request, pk):
        todo = Tasks.objects.get(pk=pk)
        serializer = TodoSerializer(data=request.data, instance=todo, partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        todo = Tasks.objects.get(pk=pk)
        todo.delete()
        return Response(None)


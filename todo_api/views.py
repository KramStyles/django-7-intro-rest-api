from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

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
            item.save()
        return Response(todo.data)

    def delete(self, request):
        Tasks.objects.all().delete()
        return Response(None)

class TodoSingle(APIView):
    pass

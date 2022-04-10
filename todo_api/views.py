from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Tasks
from .serializers import TodoSerializer

class TodoList(APIView):
    def post(self, request):
        todo = TodoSerializer(request.data)
        return Response(todo.data)

class TodoSingle(APIView):
    pass

from django.urls import path, include
from rest_framework import routers

from . import views

route = routers.DefaultRouter()
route.register('v', views.TodoView)

urlpatterns = [
    path('', views.TodoList.as_view()),
    path('<int:pk>', views.TodoSingle.as_view(), name='todo-single'),
    path('', include(route.urls))
]

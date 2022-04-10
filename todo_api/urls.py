from django.urls import path

from . import views

urlpatterns = [
    path('', views.TodoList.as_view()),
    path('int:<pk>', views.TodoSingle.as_view())
]

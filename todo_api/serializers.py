from rest_framework import serializers

from .models import Tasks

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Tasks
        fields = ('id', 'title', 'url', 'finished', 'order')
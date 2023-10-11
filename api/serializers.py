from rest_framework import serializers
from . models import Todo

class TodoSerializers(serializers.ModelSerializer):

    class Meta:
        fields = (
            'id',
            'title',
            'description',
            'date',
            'completed'
        )
        model = Todo
        
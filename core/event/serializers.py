from rest_framework import serializers 
from rest_framework.exceptions import ValidationError 

from core.abstract.serializers import AbstractSerializer 
from core.event.models import Event 
from core.user.models import User 


class EventSerializer(AbstractSerializer):
    author = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='public_id')

    def validate_author(self, value):
        if self.context["request"].user != value:
            raise ValidationError("You cant create an event for another user")
        return value 
    
    class Meta:
        model = Event 
        #list all the fields that will be included in a req or response 
        fields = ['id', 'author', 'body', 'edited', 'created', 'date', 'updated']
        read_only_fields = ['edited']
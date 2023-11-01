from rest_framework import serializers 
from rest_framework.exceptions import ValidationError 

from core.abstract.serializers import AbstractSerializer 
from core.event.models import Event 
from core.user.models import User 
from core.user.serializers import UserSerializer

class EventSerializer(AbstractSerializer):
    author = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='public_id')
    liked = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    attending = serializers.SerializerMethodField()
    attending_count = serializers.SerializerMethodField()

    def validate_author(self, value):
        if self.context["request"].user != value:
            raise ValidationError("You cant create an event for another user")
        return value 
    

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        author = User.objects.get_object_by_public_id(rep['author'])
        rep["author"] = UserSerializer(author).data
        return rep
    

    def update(self, instance, validated_data):
        if not instance.edited:
            validated_data['edited'] = True 
        
        instance = super().update(instance, validated_data)
        return instance
    
    def get_attending(self, instance):
        request = self.context.get('request', None)

        if request is None or request.user.is_anonymous:
            return False 
        return request.user.has_attending(instance)
    
    def get_attending_count(self, instance):
        return instance.attending_by.count()
    
    def get_liked(self, instance):
        request = self.context.get('request', None)

        if request is None or request.user.is_anonymous:
            return False
        return request.user.has_liked(instance)
    
    def get_likes_count(self, instance):
        return instance.liked_by.count()
    class Meta:
        model = Event 
        #list all the fields that will be included in a req or response 
        fields = ['id', 'author', 'body', 'edited', 'created', 'date', 'updated', 'liked', 'likes_count', 'attending', 'attending_count']
        read_only_fields = ['edited']
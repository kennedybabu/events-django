from rest_framework import serializers
from rest_framework.exceptions import ValidationError 


from core.abstract.serializers import AbstractSerializer 
from core.user.models import User 
from core.user.serializers import UserSerializer 
from core.blog.models import Blog 


class BlogSerializer(AbstractSerializer):
    author = serializers.SlugRelatedField(queryset = User.objects.all(), slug_field='public_id')

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        author = User.objects.get_object_by_public_id(rep['author'])
        rep['author'] = UserSerializer(author).data 

        return rep
    
    class Meta:
        model = Blog
        fields = ['id', 'author', 'body', 'edited', 'created', 'updated', 'title']
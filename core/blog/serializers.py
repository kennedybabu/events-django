from rest_framework import serializers
from rest_framework.exceptions import ValidationError 


from core.abstract.serializers import AbstractSerializer 
from core.user.models import User 
from core.user.serializers import UserSerializer 
from core.blog.models import Blog 
from django.conf import settings



class BlogSerializer(AbstractSerializer):
    author = serializers.SlugRelatedField(queryset = User.objects.all(), slug_field='public_id')

    def validate_author(self, value):
        if self.context['request'].user != value:
            raise ValidationError("You can't create a blog for another user")
        return value

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        author = User.objects.get_object_by_public_id(rep['author'])
        rep['author'] = UserSerializer(author).data 
        if not rep['banner_image']:
            rep['banner_image'] = settings.DEFAULT_EVENT_BANNER_URL
            return rep
        if settings.DEBUG:
            request = self.context.get('request')
            if request:
                rep['banner_image'] = request.build_absolute_uri(rep['banner_image'])
        return rep
    
    class Meta:
        model = Blog
        fields = ['id', 'author', 'body', 'edited', 'created', 'updated', 'title', 'banner_image']
from rest_framework import serializers
from core.user.models import User 
from core.abstract.serializers import AbstractSerializer
from django.conf import settings

class UserSerializer(AbstractSerializer):
    id = serializers.UUIDField(source='public_id', read_only=True, format='hex')
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if 'avatar' in representation and not representation['avatar']:
            representation['avatar'] = settings.DEFAULT_AVATAR_URL
            return representation
        if 'profile_background_image' in representation and not representation['profile_background_image']:
            representation['profile_background_image'] = settings.DEFAULT_PROFILE_BG_URL
            return representation
        if settings.DEBUG:
            request = self.context.get('request') 
            if request:
                representation['avatar'] = request.build_absolute_uri(representation['avatar'])
                representation['profile_background_image'] = request.build_absolute_uri(representation['profile_background_image'])
        return representation

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'bio', 'email', 'is_active', 'created', 'updated', 'avatar', 'profile_background_image']
        read_only_field = ['is_active']
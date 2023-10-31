from rest_framework import serializers

from core.user.serializers import UserSerializer 
from core.user.models import User 


class RegisterSerializer(UserSerializer):
    """Registration serializer for requests and user creation"""
    # making sure the password is at least 8 char long 
    password = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)

    class Meta:
        model = User 
        #list all the fields that can be included in a req or a response 
        fields = ['id', 'bio', 'email', 'username', 'first_name','last_name', 'password']

    def create(self, validated_data):
        #Use the `create_user` method for the user manager to create a new user 
        return User.objects.create_user(**validated_data)
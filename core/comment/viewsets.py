from core.abstract.viewsets import AbstractViewSet
from django.http.response import Http404 


from rest_framework.response import Response 
from core.comment.models import Comment 
from core.comment.serializers import CommentSerializer
from core.auth.permissions import UserPermission 
from rest_framework.decorators import action 
from rest_framework import status


class CommentViewSet(AbstractViewSet):
    http_method_names = ('post', 'get', 'delete', 'put')
    # permission_classes = (UserPermission,)
    serializer_class = CommentSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Comment.objects.all()
        
        event_pk = self.kwargs['event_pk']
        if event_pk is None:
            return Http404
        queryset = Comment.objects.filter(event__public_id=event_pk)
        return queryset
    
    def get_object(self):
        obj = Comment.objects.get_object_by_public_id(self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def validate_event(self, value):
        if self.instance:
            return self.instance.event
        return value 
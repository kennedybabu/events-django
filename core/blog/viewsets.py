from rest_framework.permissions import IsAuthenticated

from core.abstract.viewsets import AbstractViewSet 
from core.blog.models import Blog 
from core.blog.serializers import BlogSerializer 
from rest_framework.response import Response 
from rest_framework import status


class BlogViewSet(AbstractViewSet):
    http_method_names = ('post', 'get', 'delete')
    permission_classes = (IsAuthenticated,)
    serializer_class = BlogSerializer 

    def get_queryset(self):
        return Blog.objects.all()
    
    def get_object(self):
        obj = Blog.objects.get_object_by_public_id(self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
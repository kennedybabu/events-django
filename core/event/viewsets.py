from rest_framework.permissions import IsAuthenticated 

from core.abstract.viewsets import AbstractViewSet 
from core.event.models import Event 
from core.event.serializers import EventSerializer 
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django.utils import timezone

class EventViewSet(AbstractViewSet):
    http_method_names = ('post', 'get', 'put', 'delete')
    permission_classes = (IsAuthenticated,)
    serializer_class = EventSerializer 

    def list(self, request, *args, **kwargs):
        events = Event.objects.all()

        now = timezone.now()
        for event in events:
            if event.date < now and not event.due:
                event.due = True 
                event.save()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        return Event.objects.all()
    
    def get_object(self):
        obj = Event.objects.get_object_by_public_id(self.kwargs['pk'])
        self.check_object_permissions(self.request, obj)
        return obj 
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

    # attendance
    @action(methods=['post'], detail=True)
    def attend(self, request, *args, **kwargs):
        event = self.get_object()
        user = self.request.user 
        user.attend(event)

        serializer = self.serializer_class(event)
        return Response(serializer.data, status=status.HTTP_200_OK)


    @action(methods=['post'], detail=True)
    def remove_attendance(self, request, *args, **kwargs):
        event = self.get_object()
        user = self.request.user 
        user.not_attend(event)

        serializer = self.serializer_class(event)
        return Response(serializer.data, status=status.HTTP_200_OK)  


    # like actions
    @action(methods=['post'], detail=True)
    def like(self, request, *args, **kwargs):
        event = self.get_object()
        user = self.request.user
        user.like(event)

        serializer = self.serializer_class(event)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(methods=['post'], detail=True)
    def remove_like(self,request, *args, **kwargs):
        event = self.get_object()
        user = self.request.user 
        user.remove_like(event)

        serializer = self.serializer_class(event)
        return Response(serializer.data, status=status.HTTP_200_OK)
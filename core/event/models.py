from django.db import models
from datetime import date
from django.utils import timezone

# Create your models here.
from core.abstract.models import AbstractManager, AbstractModel 

class EventManager(AbstractManager):
    pass 


def user_directory_path(instance, filename):
    # MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.public_id, filename)

class Event(AbstractModel):
    author = models.ForeignKey(to='core_user.User', on_delete=models.CASCADE)
    body = models.TextField()
    edited = models.BooleanField(default=False)
    banner = models.ImageField(null=True, blank=True, upload_to=user_directory_path)
    date = models.DateTimeField()
    due = models.BooleanField(default=False)
    ticket_price = models.CharField(max_length=8, null=True)
    age_limit = models.CharField(max_length=3, null=True)

    objects = EventManager()
    def __str__(self):
        return f"{self.author.name}"  
    
    class Meta:
        db_table = "'core.event'"

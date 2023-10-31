from django.db import models

# Create your models here.
from core.abstract.models import AbstractManager, AbstractModel 

class EventManager(AbstractManager):
    pass 

class Event(AbstractModel):
    author = models.ForeignKey(to='core_user.User', on_delete=models.CASCADE)
    body = models.TextField()
    edited = models.BooleanField(default=False)
    # banner = models.
    date = models.DateTimeField()

    objects = EventManager()
    def __str__(self):
        return f"{self.author.name}"
    
    class Meta:
        db_table = "'core.event'"

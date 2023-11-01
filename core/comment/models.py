from django.db import models

# Create your models here.
from core.abstract.models import AbstractManager, AbstractModel 


class CommentManager(AbstractManager):
    pass 


class Comment(AbstractModel):
    event = models.ForeignKey("core_event.Event", on_delete=models.PROTECT)
    author = models.ForeignKey("core_user.User", on_delete=models.PROTECT)
    body = models.TextField()
    edited = models.BooleanField(default=False)

    objects = CommentManager()

    def __str__(self):
        return self.event[0:10]
from django.db import models
from core.abstract.models import AbstractModel, AbstractManager 
# Create your models here.


class BlogManager(AbstractManager):
    pass 

def user_directory_path(instance, filename):
    # MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.public_id, filename)


class Blog(AbstractModel):
    title = models.CharField(max_length=255)
    # event = models.ForeignKey("core_event.Event", on_delete=models.PROTECT)
    author = models.ForeignKey("core_user.User", on_delete=models.PROTECT)
    body = models.TextField()
    edited = models.BooleanField(default=False)
    banner_image = models.ImageField(null=True, blank=True, upload_to=user_directory_path)


    objects = BlogManager()

    def __str__(self):
        return self.author.name

from django.db import models
import uuid 
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin 
from django.core.exceptions import ObjectDoesNotExist 
from django.db import models 
from django.http import Http404
from core.abstract.models import AbstractManager, AbstractModel

# Create your models here.
class UserManager(BaseUserManager, AbstractManager):
    def get_object_by_public_id(self, public_id):
        try:
            instance = self.get(public_id=public_id)
            return instance
        except (ObjectDoesNotExist, ValueError, TypeError):
            return Http404
        
    def create_user(self, username, email, password=None, **kwargs):
        """create and return user with email, phone no, username and password"""
        if username is None:
            raise TypeError('Users must hava a username')
        if email is None:
            raise TypeError("Users must have an email")
        if password is None:
            raise TypeError("users must have a password")
        
        user = self.model(username=username, email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user



    def create_superuser(self, username, email, password, **kwargs):
        """create and return a `User` with superadmin permissions"""
        if password is None:
            raise TypeError('Superusers must have a password')
        if email is None:
            raise TypeError("Superusers must have an email")
        if username is None:
            raise TypeError('Superusers must have a username')
        
        user = self.create_user(username, email, password, **kwargs)
        user.is_superuser = True
        user.is_staff = True 
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin, AbstractModel):
    public_id = models.UUIDField(db_index=True, unique=True, default=uuid.uuid4,editable=False)
    username = models.CharField(db_index=True, max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255) 
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    bio = models.TextField(null=True)
    events_liked = models.ManyToManyField("core_event.Event", related_name='liked_by')
    events_attending = models.ManyToManyField("core_event.Event", related_name='attending_by')


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return f"{self.email}"
    
    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"
    


    def attend(self, event):
        """Show interest in attendning the event"""
        return self.events_attending.add(event)    

    def not_attend(self, event):
        """Remove name from list of the attendees"""
        return self.events_attending.remove(event)
    
    def has_attending(self, event):
        """Return True if the user is attending the event;else False"""
        return self.events_attending.filter(pk=event.pk).exists()
    

    #event methods 
    def like(self, event):
        """Like a `event` if it hasnt been done yet"""
        return self.events_liked.add(event)

    def remove_like(self, event):
        """Remove a like from an event"""
        return self.events_liked.remove(event) 
    
    def has_liked(self, event):
        """Return True if the user has liked an event; else False"""
        return self.events_liked.filter(pk=event.pk).exists()


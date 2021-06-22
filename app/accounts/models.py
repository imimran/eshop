from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
import uuid
import os

def user_image_path(instance, filename):
    """ Genereate image path for recipe"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('user/', filename)

class UserManager(BaseUserManager):
    def create_user(self, email, phone, password=None):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError('Users Must Have A Email')
        if not phone:
            raise ValueError('Users Must Have A Phone Number')
    
     
        email = self.normalize_email(email)
        user = self.model(email=email, phone=phone)
        user.set_password(password)
        user.is_staff = False
        user.save(using=self._db)
        return user  

    def create_superuser(self, email, phone, password=None):
        """
        Create and save a SuperUser with the given email and password.
        """
        
        if not email:
            raise ValueError('email is requried')
        email = self.normalize_email(email)
        user = self.model(email=email, phone= phone)
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Role(models.Model):
    
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=5)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name       

class User(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.IntegerField()
    address = models.TextField(max_length=1000)
    image = models.ImageField(blank=True, upload_to=user_image_path)
    is_active = models.BooleanField(default=True)
    username = None
    updated_at = models.DateTimeField(auto_now=True)
    role = models.OneToOneField(Role, on_delete=models.CASCADE, blank=True, null=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone']

    objects = UserManager()
    
    def __str__(self):
        return self.email



from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
from django.conf import settings
# Create your models here.





class User(AbstractBaseUser):
    """
    Description:This is going to be the main User Model
    """
    email = models.EmailField(verbose_name='email address',max_length=255,unique=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    timestamp = models.DateTimeField(auto_now_add=True)


    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    
    def get_short_name(self):
         # The user is identified by their email address
         return self.email

    
    def has_perm(self,perm,obj=None):
        #Does the user have a specific permission?
        # Simplest possible answer: Yes, always
        return True
    

    def has_module_perms(self, app_label):
        #"Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    
    @property
    def is_staff(self):
        #"Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        #"Is the user an admin member?"
        return self.admin
    
    @property
    def is_active(self):
        "Is the user active?"
        return self.active




class GuestEmail(models.Model):
    email = models.EmailField()
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.email
from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
from django.conf import settings
# Create your models here.



class UserManager(BaseUserManager):
    def create_user(self,email,full_name=None,password=None,is_active=True,is_staff=False,is_admin=False):
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Users must have a password")
        user_obj = self.model(
            email=self.normalize_email(email),
            full_name = full_name
        )
        user_obj.set_password(password)
        user_obj.staff=is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using=self._db)
        return user_obj

    

    def create_staffuser(self,email,full_name=None,password=None):
        user = self.create_user(
            email,
            full_name=full_name,
            password=password,
            is_staff=True
        )
        return user

    
    def create_superuser(self,email,full_name=None,password=None):
        user = self.create_user(
            email,
            full_name=full_name,
            password=password,
            is_staff=True,
            is_admin=True
        )
        return user








class User(AbstractBaseUser):
    """
    Description:This is going to be the main User Model
    """
    email = models.EmailField(verbose_name='email address',max_length=255,unique=True)
    full_name = models.CharField(max_length=200,blank=True, null=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    timestamp = models.DateTimeField(auto_now_add=True)


    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        # The user is identified by their email address or full name
        if self.full_name:
            return self.full_name
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
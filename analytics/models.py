from django.db import models

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


from django.conf import settings

User = settings.AUTH_USER_MODEL



class ObjectViewed(models.Model):
    """
    Description:Represent user interactions with the app.\n
    """
    user = models.ForeignKey(User,blank=True, null=True)
    ip_address = models.CharField(max_length=200,blank=True, null=True)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type','object_id')
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return "%s viewed %s" %(Self.content_object,self.timestamp)

    
    class Meta:
        ordering = ['-timestamp']
        verbose_name = 'Object Viewed'
        verbose_name_plural = 'Objects Viewed'

        

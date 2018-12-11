from django.db import models

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from .signals import object_viewed_signal
from .utils import get_client_ip_address
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
        return "%s viewed %s" %(self.content_object,self.timestamp)

    
    class Meta:
        ordering = ['-timestamp']
        verbose_name = 'Object Viewed'
        verbose_name_plural = 'Objects Viewed'

        







def object_viewed_receiver(sender,instance,request,*args,**kwargs):
    c_type = ContentType.objects.get_for_model(sender) # instance.__class__
    user_ip = get_client_ip_address(request)
    user = None
    if request.user.is_authenticated():
        user = request.user
    
    new_view_obj = ObjectViewed.objects.create(
        user = user,
        content_type=c_type,
        object_id=instance.id,
        ip_address = user_ip
    )




object_viewed_signal.connect(object_viewed_receiver)
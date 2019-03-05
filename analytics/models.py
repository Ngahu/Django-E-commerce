from django.db import models

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from .signals import object_viewed_signal
from .utils import get_client_ip_address
from django.conf import settings
from django.contrib.sessions.models import Session
from django.db.models.signals import pre_save,post_save
from accounts.signals import user_logged_in

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




class UserSession(models.Model):
    '''
    Description:store a users session 
    '''
    user = models.ForeignKey(User,blank=True, null=True)
    ip_address = models.CharField(max_length=200,blank=True, null=True)
    session_key = models.CharField(max_length=200,blank=True, null=True)
    active = models.BooleanField(default=True)
    ended = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)


    def end_session(self):
        the_key = self.session_key
        ended = self.ended
        try:
            Session.objects.get(pk=the_key).delete()
            self.active = False
            self.ended = True
            self.save() 
        
        except:
            print("Key not found")
            pass
        return self.ended
        
        



def post_save_session_receiver(sender,instance,created,*args,**kwargs):
    if created:
        qs = UserSession.objects.filter(user=instance.user,ended=False,active=False).exclude(id=instance.id) #exclude the current session_key
        for i in qs:
            i.end_session()




post_save.connect(post_save_session_receiver,sender=UserSession)









def user_logged_in_receiver(sender,instance,request,*args,**kwargs):
    print(instance)

    user = instance
    user_ip = get_client_ip_address(request)
    session_key = request.session.session_key
    UserSession.objects.create(
        user = user,
        ip_address=user_ip,
        session_key = session_key,
    )



user_logged_in.connect(user_logged_in_receiver)
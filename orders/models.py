from django.db import models

# Create your models here.
from cart.models import Cart
from django.db.models.signals import pre_save

from .utils import unique_order_id_generator

ORDER_STATUS_CHOICES = (
    ('created','Created'),
    ('paid','Paid'),
    ('shipped','Shipped'),
    ('refunded','Refunded')
)



class Order(models.Model):
    """
    """
    cart = models.ForeignKey(Cart)
    status = models.CharField(max_length=120,default='created',choices=ORDER_STATUS_CHOICES)
    order_id = models.CharField(max_length=120,unique=True,blank=True)
    shipping_total = models.DecimalField(default=5.99,max_digits=100,decimal_places=2) #like a delivery total if it requires delivery
    total = models.DecimalField(default=0,max_digits=100,decimal_places=2)

    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.order_id




def pre_save_create_order_id(sender,instance,*args,**kwargs):
    if not instance.order_id:
        instance.order_id = unique_order_id_generator(instance)



pre_save.connect(pre_save_create_order_id,sender=Order)

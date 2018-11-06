from django.db import models
from django.db.models.signals import pre_save
from products.utils import unique_slug_generator
from products.models import Product
# Create your models here.



class Tag(models.Model):
    """
    Description:
    """
    title = models.CharField(max_length=150)
    slug = models.SlugField()
    active = models.BooleanField(default=True)
    products = models.ManyToManyField(Product,blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title



def tag_pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(tag_pre_save_receiver,sender=Tag)
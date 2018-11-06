import os
import random
from django.db import models
from .utils import unique_slug_generator
from django.db.models.signals import pre_save
from django.core.urlresolvers import reverse
from django.db.models import Q

# Create your models here.

def get_filename_ext  (filepath):
    base_name = os.path.basename(filepath)
    name,ext = os.path.splitext(base_name)
    return name,ext 


def upload_image_path(instance,filename):
    print(instance)
    print(filename)
    new_filename = random.randint(1,1234567890)
    name,ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename,ext=ext)
    return "products/{new_filename}/{final_filename}".format(new_filename=new_filename,final_filename=final_filename )



class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def featured(self):
        return self.filter(featured=True,active=True)

    def search(self,query):
        lookups = (Q(title__icontains=query) |
                   Q(description__icontains=query) |
                   Q(price__icontains=query) |
                   Q(tag__title__icontains=query) |
                   Q(tag__description__icontains=query)
                   )
        return self.filter(lookups).distinct()




class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model,using=self._db)

    def all(self):
        return self.get_queryset().active()

    def featured(self):
        return self.get_queryset().featured()

    def get_by_id(self,id):
        return self.get_queryset().filter(id=id)

    
    def search(self,query):
        """
        Description:Perform the search by the user 
        """
        return self.get_queryset().active().search(query)



class Product(models.Model):
    """
    """
    title = models.CharField(max_length=100)
    slug =models.SlugField(unique=True,blank=True)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2,max_digits=20)
    image = models.ImageField(upload_to=upload_image_path,blank=True, null=True)
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    objects = ProductManager()


    def __str__(self):
        return self.title

    
    def get_absolute_url(self):
        return reverse("products:product_detail", kwargs={"slug": self.slug})
        




def product_pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(product_pre_save_receiver,sender=Product)
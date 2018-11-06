from django.db import models
from django.conf import settings

from products.models  import Product
User = settings.AUTH_USER_MODEL

# Create your models here.


class CartManager(models.Manager):
    def new(self,user=None,products=None):
        """
        Description:Create a new cart.\n
        """
        user_obj = None
        if user is not None:
            if user.is_authenticated():
                user_obj = user
        created_cart = self.model.objects.create(user=user_obj)
        return created_cart



class Cart(models.Model):
    """
    Description:Store a cart belonging to a user.\n
    """
    user = models.ForeignKey(User,blank=True, null=True)
    products = models.ManyToManyField(Product,blank=True)
    total = models.DecimalField(default=0.00,max_digits=100,decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = CartManager()

    def __str__(self):
        return str(self.id)
from django.db import models
from django.conf import settings

from products.models  import Product
User = settings.AUTH_USER_MODEL

# Create your models here.


class CartManager(models.Manager):

    def new_or_get(self,request):
        cart_id = request.session.get("cart_id", None)
        qs = Cart.objects.filter(id=cart_id)
        if qs.count() ==1:
            new_obj = False
            cart_obj = qs.first()
            if request.user.is_authenticated() and cart_obj.user is None:
                cart_obj.user = request.user
                cart_obj.save()
        else:
            #create a new cart
            cart_obj = Cart.objects.new(user=request.user)
            new_obj = True
            request.session['cart_id'] = cart_obj.id
        
        return cart_obj,new_obj



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
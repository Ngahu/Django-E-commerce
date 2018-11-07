from django.shortcuts import render,redirect

# Create your views here.
from .models import Cart
from products.models import Product


def cart_home(request):
    cart_obj,new_obj = Cart.objects.new_or_get(request)
    template_name = 'cart/cart.html'
    context = {}
    return render(request,template_name,context)





def cart_update(request):
    product_obj = Product.objects.get(id=1)
    cart_obj,new_obj = Cart.objects.new_or_get(request)
    if product_obj in cart_obj.products.all():
        cart_obj.products.remove(product_obj)
    else:
        cart_obj.products.add(product_obj)
    # return redirect(product_obj.get_absolute_url())
    return redirect("cart:cart_home")

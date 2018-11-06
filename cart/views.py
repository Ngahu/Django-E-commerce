from django.shortcuts import render

# Create your views here.
from .models import Cart



def cart_create(user=None):
    """
    Description:Create a new cart.\n
    """
    cart_obj = Cart.objects.create(user=None)
    print("Cart is Created")
    return cart_obj



def cart_home(request):
    cart_id = request.session.get("cart_id", None)
    qs = Cart.objects.filter(id=cart_id)
    if qs.count() ==1:
        print("Cart exists")
        cart_obj = qs.first()
    else:
        #create a new cart
        cart_obj = cart_create()
        request.session['cart_id'] = cart_obj.id

    template_name = 'cart/cart.html'
    context = {}
    return render(request,template_name,context)
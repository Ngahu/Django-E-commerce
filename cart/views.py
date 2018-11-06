from django.shortcuts import render

# Create your views here.
from .models import Cart

def cart_home(request):
    cart_id = request.session.get("cart_id", None)
    qs = Cart.objects.filter(id=cart_id)
    if qs.count() ==1:
        print("Cart exists")
        cart_obj = qs.first()
        if request.user.is_authenticated() and cart_obj.user is None:
            cart_obj.user = request.user
            cart_obj.save()
    else:
        #create a new cart
        cart_obj = Cart.objects.new(user=request.user)
        request.session['cart_id'] = cart_obj.id

    template_name = 'cart/cart.html'
    context = {}
    return render(request,template_name,context)
from django.shortcuts import render,redirect

# Create your views here.
from .models import Cart
from products.models import Product
from orders.models import Order
from billing.models import BillingProfile
from  accounts.forms import GuestForm,UserLoginForm

def cart_home(request):
    cart_obj,new_obj = Cart.objects.new_or_get(request)
    template_name = 'cart/cart.html'
    context = {
        "cart":cart_obj,
    }
    return render(request,template_name,context)





def cart_update(request):
    product_id = request.POST.get('product_id')
    if product_id is not None:
        try:
            product_obj = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            print("Product doesn't exist")
            return redirect("cart:cart_home")

        cart_obj,new_obj = Cart.objects.new_or_get(request)
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
        else:
            cart_obj.products.add(product_obj)
        request.session['cart_items'] = cart_obj.products.count()
    # return redirect(product_obj.get_absolute_url())
    return redirect("cart:cart_home")






def checkout_home(request):
    cart_obj,cart_created = Cart.objects.new_or_get(request)
    order_obj = None
    if cart_created or cart_obj.products.count() == 0:
        return redirect("cart:cart_home")
    else:
        order_obj,new_order_obj = Order.objects.get_or_create(cart=cart_obj)
    
    guest_form = GuestForm()
    user = request.user
    billing_profile = None   

    login_form = UserLoginForm()

    if user.is_authenticated():
        billing_profile, billing_profile_created = BillingProfile.objects.get_or_create(
                                                            user=user,
                                                            email=user.email
                                                            )

    
    context = {
        "order":order_obj,
        "billing_profile":billing_profile,
        "login_form":login_form
    }

    template_name = 'cart/checkout.html'
    return render(request,template_name,context)
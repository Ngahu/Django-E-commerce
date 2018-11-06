from django.shortcuts import render

# Create your views here.
from .models import Cart

def cart_home(request):
    cart_obj = Cart.objects.new_or_get(request)
    template_name = 'cart/cart.html'
    context = {}
    return render(request,template_name,context)
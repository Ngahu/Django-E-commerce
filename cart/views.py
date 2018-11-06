from django.shortcuts import render

# Create your views here.


def cart_home(request):
    cart_id = request.session.get("cart_id", None)
    if cart_id is None:
        print("Cart is none.Create one")
        pass
    else:
        print("Cart exists")




    template_name = 'cart/cart.html'
    context = {}
    return render(request,template_name,context)
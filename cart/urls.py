from django.conf.urls import url

from .views import (
    cart_home,
    cart_update
)



urlpatterns = [
    url(r'^home/$',cart_home,name='cart_home'),
    url(r'^cart-update/$',cart_update,name='cart_update'),
    # url(r'^products/(?P<slug>[\w-]+)/$',ProductDetailView.as_view(),name='product_detail'),
]
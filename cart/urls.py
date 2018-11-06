from django.conf.urls import url

from .views import (
    cart_home
)



urlpatterns = [
    url(r'^home/$',cart_home,name='cart_home'),
    # url(r'^products/(?P<slug>[\w-]+)/$',ProductDetailView.as_view(),name='product_detail'),
]
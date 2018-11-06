from django.conf.urls import url

from .views import (
    ProductListView,
    ProductDetailView
)



urlpatterns = [
    url(r'^product-list/$',ProductListView.as_view(),name='product_list'),
    url(r'^products/(?P<slug>[\w-]+)/$',ProductDetailView.as_view(),name='product_detail'),
]
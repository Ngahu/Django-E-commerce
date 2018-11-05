from django.conf.urls import url

from .views import (
    ProductListView
)



urlpatterns = [
    url(r'^products-list/$',ProductListView.as_view(),name='product_list'),
]
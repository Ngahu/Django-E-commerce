from django.conf.urls import url

from .views import (
    SearchProductView  
)



urlpatterns = [
    url(r'^$',SearchProductView.as_view(),name='product_search'),
    # url(r'^products/(?P<slug>[\w-]+)/$',ProductDetailView.as_view(),name='product_detail'),
]
from django.shortcuts import render
from django.views.generic.list import ListView


from .models import Product





class ProductListView(ListView):
    """
    Description:Return a list of all products in the database.\n
    """
    queryset = Product.objects.all()
    template_name = 'products/product_list.html'


    def get_context_data(self,*args,**kwargs):
        context = super(ProductListView,self).get_context_data()
        print (context)
        return context

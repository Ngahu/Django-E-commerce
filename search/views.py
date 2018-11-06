from django.shortcuts import render
from products.models import Product
from django.views.generic import ListView

# Create your views here.




class SearchProductView(ListView):
    """
    Description:Return a list of all products in the database.\n
    """
    queryset = Product.objects.all()
    template_name = 'products/product_list.html'


    def get_queryset(self,*args,**kwargs):
        request = self.request

        query = request.GET.get('q')
        print(query)
        if query is not None:
            return Product.objects.filter(title__icontains=query)
        
        return Product.objects.none()
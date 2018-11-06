from django.shortcuts import render
from products.models import Product
from django.views.generic import ListView

# Create your views here.




class SearchProductView(ListView):
    """
    Description:Return a list of all products in the database.\n
    """
    queryset = Product.objects.all()
    template_name = 'search/view.html'


    def get_queryset(self,*args,**kwargs):
        request = self.request

        query = request.GET.get('q',None)
        print(query)
        if query is not None:
            return Product.objects.search(query)
        
        # return Product.objects.all()
        return Product.objects.featured()
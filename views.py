from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from product_module.models import Product


# Create your views here.



def product_list(request):
    products = Product.objects.filter(is_active=True)
    return render(request , 'product_list.html',{
        'products':products
    })
def product_detail(request,slug):
    detail = get_object_or_404(Product,slug=slug)
    return render(request , 'product_detail.html',{
        'product': detail
    })
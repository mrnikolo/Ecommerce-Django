from django.shortcuts import render, get_object_or_404
from .models import Product
from . import models

# Create your views here.

def shop(request):
    products = Product.objects.order_by('-create_at')
    context = {'products': products}
    return render(request, 'shop.html' , context)

# pk = primary key ==> for get id any object
def product(request, pk):
    product_details = get_object_or_404(models.Product, id=pk)
    context = {'product_details': product_details}
    return render(request, 'product.html' , context)



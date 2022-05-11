from django.shortcuts import render
from .models import Product

# Create your views here.

def all_products(request):
    """ This view shows all products, and sorts in their categories """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
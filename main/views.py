from django.shortcuts import render, get_object_or_404
from .models import Product


# Create your views here.
def home(request):
    try:
        products = Product.objects.all()
    except Product.DoesNotExist:
        products = []
    return render(request, 'main/index.html', {'products': products})


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'main/product_detail.html', {'product': product})

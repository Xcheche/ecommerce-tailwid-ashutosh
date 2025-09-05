from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages

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



# New view to add a product    
def add_product(request):
    errors = {}
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        product_image = request.FILES.get('image')  # Fix key here

        # Validate fields
        if not name:
            errors['name'] = 'Name is required.'
        if not description:
            errors['description'] = 'Description is required.'
        try:
            price_val = float(price)
        except (ValueError, TypeError):
            errors['price'] = 'Valid price is required.'
        if not product_image:
            errors['image'] = 'Product image is required.'

        if not errors:
            try:
                product = Product(
                    name=name,
                    description=description,
                    price=price_val,
                    product_image=product_image
                )
                product.save()
                messages.success(request, 'Product added successfully!')
                return render(request, 'main/add_product.html')
            except Exception as e:
                errors['database'] = str(e)

    return render(request, 'main/add_product.html', {'errors': errors})

#Update view

def update(request, id):
    product = get_object_or_404(Product, id=id)
    errors = {}
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        product_image = request.FILES.get('image')  # Fix key here

        # Validate fields
        if not name:
            errors['name'] = 'Name is required.'
        if not description:
            errors['description'] = 'Description is required.'
        try:
            price_val = float(price)
        except (ValueError, TypeError):
            errors['price'] = 'Valid price is required.'
        if not product_image:
            errors['image'] = 'Product image is required.'

        if not errors:
            try:
                product.name = name
                product.description = description
                product.price = price_val
                product.product_image = product_image
                product.save()
                messages.success(request, 'Product updated successfully!')
                return render(request, 'main/add_product.html', {'product': product})
            except Exception as e:
                errors['database'] = str(e)

    return render(request, 'main/add_product.html', {'errors': errors, 'product': product})



#Delete view
def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    context = {
        'product': product
    }
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted successfully!')
        return redirect('home')
    return render(request, 'main/delete.html', context)
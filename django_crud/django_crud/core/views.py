from django.shortcuts import render, redirect
from .models import Product

# Create your views here.
def list_products(request):
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(request,'products.html', context=context)

def create_products(request):
    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_products')
    
    return render(request, 'products')
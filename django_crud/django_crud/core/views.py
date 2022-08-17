from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

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
    
    context = {
        'form':form
    }
    return render(request, 'products_form.html', context=context)

def update_products(request, id):
    product = Product.objects.get(id=id)
    form = ProductForm(request.POST or None, instance=product) #instance product serve para que o form já venha como instância de produto e preenchido
    if form.is_valid():
        form.save()
        return redirect('list_products')

    context = {
        'form':form,
        'product': product
    }
    return render(request, 'products_form.html', context=context)

def delete_products(request, id):
    product = Product.objects.get(id=id)

    if request.method == 'POST':
        product.delete()
        return redirect('list_products')

    context = {
        'product': product
    }
    return render(request, 'prod_delete_confirm.html', context=context)
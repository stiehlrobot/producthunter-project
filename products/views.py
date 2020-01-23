from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Product

# Create your views here.
def home(request):
    return render(request, 'products/home.html')

@login_required
def create(request):
    return render(request, 'products/create.html')
    
'''
def present(request):

    products = Product.objects
    return render(request, 'product/presentproducts.html', {'products':products})

def productdetail(request):

    product_detail = get_object_or_404(Product, pk=product_id)
    return render(request, 'product/productdetail.html', {'product':product_detail})

'''
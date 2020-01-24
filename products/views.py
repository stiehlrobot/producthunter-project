from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import Product

# Create your views here.
def home(request):
    return render(request, 'products/home.html')

@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
            product = Product()
            product.title = request.POST['title']
            product.body = request.POST['body']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                product.url = request.POST['url']
            else:
                product.url = 'http://' + request.POST['url']
            product.icon = request.FILES['icon']
            product.icon = request.FILES['image']
            product.pub_date = timezone.datetime.now()            
            product.hunter = request.user
            product.save()
            return redirect('/products/' + str(product.id))

        else:
            return render(request, 'products/create.html', {'error':'All fields must be filled'})
    return render(request, 'products/create.html')
    

def detail(request, product_id):

    product_detail = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/detail.html', {'product':product_detail})

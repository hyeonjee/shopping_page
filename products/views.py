from django.shortcuts import render, redirect, get_object_or_404
from .models import Product

# Create your views here.
def home(request):
    return render(request, 'products/home.html')

def main(request):
    products=Product.objects.all()
    return render(request, 'products/main.html', {'products':products})


def new(request):
    return render(request, 'products/new.html')

def create(request):
    if request.method == "POST":
        product_name = request.POST.get('product_name')
        product_info = request.POST.get('product_info')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        image = request.FILES.get('image')
        seller = request.user
        Product.objects.create(product_name=product_name, product_info=product_info, price=price, stock=stock, image=image, seller=seller)
    return redirect ('products:main')

def show(request, id):
    product = get_object_or_404(Product, pk=id)
    product.save()
    return render (request, 'products/show.html', {"product":product})

def update(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == "POST":
        product.product_name = request.POST['product_name']
        product.product_info = request.POST['product_info']
        product.price = request.POST['price']
        product.stock = request.POST['stock']
        product.image = request.FILES.get('image')
        product.seller = request.user
        product.save()
        return redirect('products:show', product.pk)
    return render(request, 'products/edit.html', {'product':product})

def delete(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return redirect('products:main')
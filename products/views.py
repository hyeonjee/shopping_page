from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *

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
    # product.view_count += 1
    product.save()
    reviews = product.comments.all().order_by('-created_at')
    return render (request, 'products/show.html', {"product":product, "reviews":reviews})

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

def create_review(request, product_id):
    if request.method == "POST":
        product = get_object_or_404(Product, pk =product_id)
        writer = request.user
        # rating = request.POST.get('rating')
        review_content = request.POST.get('content')
        Review.objects.create(content = review_content, writer = writer, product=product)
    return redirect('products:show', product.pk)

def delete_review(request, review_id):
    review = get_object_or_404(Review, pk = review_id)
    review.delete()
    return redirect('products:main')

def update_review(request, review_id):
    review = get_object_or_404(Review, pk = review_id)
    if request.method == "POST":
        review.content = request.POST['review_content']
        review.save()
        return redirect('products:main')
    return render(request, 'products/edit_review.html', {'review':review})


@login_required
def product_like(request, product_id):
    product = get_object_or_404(Product, pk = product_id)

    if request.user in product.like_user_set.all():
        product.like_user_set.remove(request.user)
    
    else: 
        product.like_user_set.add(request.user)

    if request.GET.get('redirect_to') == 'show':
        return redirect('products:show', product_id)

    else: 
        return redirect('products:main')

@login_required
def like_list(request):
    likes = Like.objects.filter(user=request.user)
    return render(request, 'products/like_list.html', {'likes': likes})




from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'products/main.html')

def item_category(request):
    return render(request, 'products/item_category.html')

def new(request):
    return render(request, 'products/new.html')

def show(request):
    return render(request, 'products/show.html')
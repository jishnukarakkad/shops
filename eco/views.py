from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

from .models import Product

def product_list(request):
    products = Product.objects.all()  # Fetch all products from the database
    return render(request, 'product_list.html', {'products': products})
def category(request):
    return render(request,'category')
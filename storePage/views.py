from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from storeAdmin.models import StoreManager

# Create your views here.
def store(request):
    products = Product.objects.all()
    managers = StoreManager.objects.all()
    return render(request, 'store.html', {'products':products,'managers':managers})

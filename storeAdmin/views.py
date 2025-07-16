from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotAllowed
from storePage.models import Product
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import StoreManager
from django.contrib.auth.models import User

## Login as old Store Manager
def login_view(request):
  
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('product')        

    return render(request,"login.html")


## Register a new Store Manager
def register(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, 'register.html')
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        # Auto-login the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)        
            return redirect('launch')

    return render(request, 'register.html')

# Launch Your Store:
@login_required
def launch(request):

    if request.method=='POST':
        name = request.POST.get('name')
        storename = request.POST.get('storename')
        whatsapp = request.POST.get('whatsapp')

        user = request.user # get current logged user

        if StoreManager.objects.filter(user=user).exists():
            messages.error(request, "Store already launched")
            return redirect('product')

        manager = StoreManager(
            user = user,
            name = name,
            storename = storename,
            username = user.username,
            email = user.email,
            whatsapp = whatsapp
        )

        manager.save()
        return redirect('product')
    
    return render(request, 'launch.html')
    

# This function is for adding new product and display admin template
@login_required
def product(request):
    show_alert = False

    products = Product.objects.all()
    managers = StoreManager.objects.all()

    if request.method == "POST":  # if the submit button is clicked -> then we save the product
        pName = request.POST.get("pName")
        pDescription = request.POST.get("pDescription")
        pPrice = request.POST.get("pPrice")

        product = Product( # we create a new object name product for 'Product' model
            pName = pName,
            pDescription = pDescription,
            pPrice = pPrice,
        )

        product.save() 
        show_alert = True
        return redirect('product') # then we redirect to the url pattern having name = 'product'
    return render(request,'productForm.html',{'show_alert':show_alert, 'products':products, 'managers':managers}) # if post isn't called we render the 'productForm.html' template and all the products in Product module(database).

# This function is for deleting the product
@login_required
def delete_product(request,product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id) # if we find the data with the id = product_id, then we store it in product object
        product.delete() # we now delete the product object
    return redirect('product')

# This function is for updating the product
@login_required
def update_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    managers = StoreManager.objects.all()

    if request.method == 'POST':
        product.pName = request.POST.get('pName')
        product.pDescription = request.POST.get('pDescription')
        product.pPrice = request.POST.get('pPrice')
        product.save()
        return redirect('product')
    return render(request, 'update_product.html',{'product':product,'managers':managers})

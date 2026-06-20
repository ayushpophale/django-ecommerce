from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Product
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

@login_required
def index(request):
    return render(request,'index.html')


@login_required
def home(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

# add_product start

@login_required
def add_product(request):
    if request.method == "POST":
        id = request.POST.get('ID')
        name = request.POST.get('name')
        category = request.POST.get('category')
        brand = request.POST.get('brand')
        description = request.POST.get('description')
        price = request.POST.get('price')
        image = request.FILES.get('image')
        pdfs = request.FILES.get('pdfs')

        Product.objects.create(
            ID=id,
            name=name,
            category=category,
            brand=brand,
            description=description,
            price=price,
            image=image,
            pdfs=pdfs
        )

        return redirect('home')

    return render(request, 'add.html')

# delete_product start

@login_required
def delete_products(request,id):
    obj = Product.objects.get(ID=id)
    obj.delete()
    return redirect('home')

# update_product start

@login_required
def update_products(request, id):
    obj = Product.objects.get(ID=id)

    if request.method == "POST":
        obj.name = request.POST.get('name')
        obj.category = request.POST.get('category')
        obj.brand = request.POST.get('brand')
        obj.description = request.POST.get('description')
        obj.price = request.POST.get('price')

        image = request.FILES.get('image')
        pdfs = request.FILES.get('pdfs')

        if image:
            obj.image = image

        if pdfs:
            obj.pdfs = pdfs

        obj.save()  

        return redirect('home')

    return render(request, 'update.html', {'product': obj})

# login start

from django.contrib import messages

# 👉 LOGIN
def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid Username or Password")

    return render(request, 'login.html')


# 👉 LOGOUT
def logout_user(request):
    logout(request)
    return redirect('login')

def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists")
            else:
                User.objects.create_user(username=username, email=email, password=password)
                return redirect('login')
        else:
            messages.error(request, "Passwords do not match")

    return render(request, 'register.html')

from django.shortcuts import render, redirect
from products.models import Product, Brand
from products.forms import ProductForm

# Create your views here.

def product_list_view(request):
    qs = Product.objects.all()
    context = {
        "objects" : qs
    }
    return render(request, "products/home.html", context)

def product_create_view(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            #Product.objects.create(**form.cleaned_data)
            return redirect("product-home")
        else:
            print("Invalid Form")
    return render(request, 'products/product_create.html', {"form" : form})

def product_update_view(request):
    form = ProductForm()
    if request.method == POST:
        pass




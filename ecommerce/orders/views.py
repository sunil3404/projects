from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
import json
from products.models import Product
from orders.models import Cart
from django.forms.models import model_to_dict
# Create your views here.


def order_list_view(request):
    context = None
    if request.POST:
       context = {
            "products" : Product.objects.filter(id=request.POST['p_id']).first()
        }
       return JsonResponse(model_to_dict(context['products']))
    return render(request, 'orders/myorder.html', context)

def save_to_cart(request):
    if request.POST:
       cart_obj = Cart.objects.all()
       c_details = int(request.POST['p_id'])
       for each in cart_obj:
           if each.product.id == c_details:
              return JsonResponse({'success' : "Product alredy exists in Cart" })
       p_cart = Product.objects.filter(id=c_details).first()
       Cart.objects.create(product=p_cart)
       return JsonResponse({'success' : f"Successfully added product {p_cart.product_name} to cart" })
    return render(request, 'orders/myorder.html', {})

def cart_list_view(request):
    qs = Cart.objects.all()
    context = {
        "objects" : qs
    }
    return render(request, 'orders/cart.html', context)


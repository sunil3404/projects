from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
import json
from products.models import Product
from orders.models import Cart, OrderItem
from django.forms.models import model_to_dict
from user.models import MyUser
from user.forms import AddressForm
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
    if request.POST and request.user.is_authenticated:
       user = MyUser.objects.filter(id = request.user.id).first()
       cart_obj = Cart.objects.all()
       c_details = int(request.POST['p_id'])
       for each in cart_obj:
           if each.product.id == c_details and each.userid.id == request.user.id:
              return JsonResponse({'success' : "Product alredy exists in Cart" })
       p_cart = Product.objects.filter(id=c_details).first()
       Cart.objects.create(product=p_cart, userid=user)
       return JsonResponse({'success' : f"Successfully added product {p_cart.product_name} to cart" })
    return render(request, 'orders/myorder.html', {})

def cart_list_view(request):
    qs = Cart.objects.filter(userid=request.user.id)
    context = {
        "objects" : qs
    }
    return render(request, 'orders/cart.html', context)

def cartItem_delete_view(request):
    if request.POST:
        qs = Cart.objects.all()
        obj_id = Cart.objects.filter(id=request.POST['c_id']).first()
        if obj_id:
            obj_id.delete()
            return JsonResponse({"Success" : "The Control was here"})
        else:
            return JsonResponse({"Failure" : "Failed"})
    return JsonResponse({"Failure" : "Cart Item does not exist"})

def save_order(request):
    user = MyUser.objects.filter(username=request.user).first()
    if request.POST:
        try:
            user.address = user.address + "|" + request.POST['address']
            user.save()
            user = MyUser.objects.filter(username=request.user).first()
        except KeyError:
            user = MyUser.objects.filter(username=request.user).first()
        cobj = request.POST.getlist('cartIds')
        qobj = request.POST.getlist('quantity')
        try:
            for cid, qty in zip(cobj, qobj):
                objcart = Cart.objects.filter(id=cid).first()
                prod = Product.objects.filter(id=objcart.product.id).first()
                options = {
                            "user_id" :  MyUser.objects.filter(id=objcart.userid.id).first(),
                            "product_id" : prod,
                            "price" : round(float(prod.product_price) * float(qty), 2),
                            "quantity" : qty
                }
                order = OrderItem.objects.filter(product_id=prod.id).first()
                if order:
                    if (order.product_id.id == objcart.product.id) and (order.order_status == "PREORDER"):
                        options['quantity'] = order.quantity + int(qty)
                        order.quantity = options['quantity']
                        order.price = round(float(prod.product_price) * float(options['quantity']), 2)
                        order.save()
                else:
                    OrderItem.objects.create(**options)
            return JsonResponse({"Success" : "Added Orders to OrderSummary Page"})
        except Exception as e:
            return JsonResponse({"Failed" : "Failed to Add orders to ordersSummary Page"})
    qs = OrderItem.objects.all()
    context = {
        "objects" : qs,
        "addresses" : user.address.split('|'),
    }
    return render(request, "orders/orderSummary.html", context)



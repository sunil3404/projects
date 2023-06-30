from django.urls import path
from orders import views


urlpatterns = [
    path("myorder/", views.order_list_view, name="myorder-details"),
    path("addtocart/", views.save_to_cart, name="save-to-cart"),
    path("mycart/", views.cart_list_view, name="mycart-details"),
    
]


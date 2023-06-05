from django.urls import path
from products import views


urlpatterns = [
    path("", views.product_list_view, name="product-home"),
    path("product_create/", views.product_create_view, name="product-create"),

]


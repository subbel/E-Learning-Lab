from Components.shoppifyPage.views import removeAllProducts
from django.contrib import admin 
from django.urls import path 

from Components.shoppifyPage.views import shoppingPage_view
from Components.shoppifyPage.views import checkout_view
from Components.shoppifyPage.views import add_product1View
from Components.shoppifyPage.views import delete_product1View

urlpatterns = [
  path('', shoppingPage_view, name="shoppifyPage"),
  path('checkout', checkout_view, name="checkoutPage"),
  path('add_product1/', add_product1View, name = "add_product1"),
  path('delete_product1/', delete_product1View, name="delete_product1"),
  #path('remove_entries/', removeAllProducts, name = "remove_allProducts")
]
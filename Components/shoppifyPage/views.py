import json
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse 
from django.http import JsonResponse
from requests import session
from Components.shoppifyPage.models import shoppingPage
from django.views.decorators.csrf import csrf_protect

# Create your views here.
def shoppingPage_view(request, *args, **kwargs): 
  website_info = {
    "shoppingPage": "Welcome to the E-Learning-Lab Shoppify Page.",
    "description": "Here you can make transactions to buy any of our products!"
  }
  return render(request, "shoppifyPage_detail.html", website_info)

@csrf_protect
def checkout_view(request):
  for object in shoppingPage.objects.all(): 
     print(object)
  shopping_cartData = shoppingPage.objects.all()
  dict = {
     'data': shopping_cartData
  }
  return render(request, "checkoutPage.html", dict)

@csrf_protect
def add_product1View(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if(data.get('message') == 'add' and data.get('product_changed') == True): 
          product_name = data.get('product_name')
          product_price = data.get('product_price')
          user = data.get('user')
          print(product_name)
          print(product_price)
          print(user)
          # create a new Product object and save it to the database
          new_product = shoppingPage(username=user, name=product_name, price=product_price)
          #session['product_changed'] = True
          new_product.save()
          # return a JSON response indicating success
          return JsonResponse({'success': True})
        else:
          print("failure")
          return JsonResponse({'success': False})
      # return a JSON response indicating failure

@csrf_protect
def delete_product1View(request): 
   if request.method == 'POST': 
      data = json.loads(request.body)
      if(data.get('message') == 'delete' and data.get('product_changed') == True): 
          product_name = data.get('product_name')
          product_price = data.get('product_price')
          user = data.get('user')
          print(user)
          print(product_name)
          print(product_price)
          shoppingPage.objects.filter(username = user, name = product_name, price = product_price).delete()
          #session['product_changed'] = True
          return JsonResponse({'success': True})
      else: 
         print("Products could not be deleted.")
         return JsonResponse({'success': False})

@csrf_protect
def removeAllProducts(request):
   print("Function to be implemented later.")
   print("For now just manually delete products in case of reload.")
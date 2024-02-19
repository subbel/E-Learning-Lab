from django.contrib import admin

from Components.shoppifyPage.models import shoppingPage

class ShoppingPageAdmin(admin.ModelAdmin):
     pass 
admin.site.register(shoppingPage, ShoppingPageAdmin)

# Register your models here.

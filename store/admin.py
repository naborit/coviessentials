from django.contrib import admin
from .models.product import Product
from .models.category import Categories
from .models.customer import Customer
from .models.orders import Order
from .models.product import Product
from .models.customer import Customer


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


class AdminCustomer(admin.ModelAdmin):
    list_display = ['first_name', 'phone', 'email']


admin.site.register(Product, AdminProduct)
admin.site.register(Categories, AdminCategory)
admin.site.register(Customer, AdminCustomer)
admin.site.register(Order)

from django.contrib import admin
from .models import *

# Register your models here.
class myOrder(admin.ModelAdmin):
    list_display =['user','status' ,'created_at']

class myOrderItem(admin.ModelAdmin):
    list_display =['order','product']




admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Order, myOrder)
admin.site.register(OrderItem, myOrderItem)
admin.site.register(Profile)

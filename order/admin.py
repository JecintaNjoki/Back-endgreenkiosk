from django.contrib import admin

# Register your models here.
from .models import Order
class OrderAdmin(admin.ModelAdmin):
    list_display=("name","customer_name","items","discount_percentage","date_created","date_updated")

admin.site.register(Order,OrderAdmin)
from django.contrib import admin

# Register your models here.
from .models import Cart
class CartAdmin(admin.ModelAdmin):
    list_display=("name","price","total_amount","date_created","date_updated")

admin.site.register(Cart,CartAdmin)  
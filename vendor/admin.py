from django.contrib import admin

# Register your models here.

from .models import Vendor
class VendorAdmin(admin.ModelAdmin):
      list_display=("first_name","last_name","email","password","date_created","date_updated")


admin.site.register(Vendor,VendorAdmin)

from django.contrib import admin

# Register your models here.
from .models import Payment
class PaymentAdmin(admin.ModelAdmin):
    list_display=("date","balance","date_created","date_updated")

admin.site.register(Payment,PaymentAdmin)
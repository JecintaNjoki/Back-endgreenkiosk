from django.urls import path 
from .views import upload_customer

urlpatterns = [
    path("customer/upload/", upload_customer, name= "upload_customer"),
]
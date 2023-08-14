from django.urls import path 
from .views import upload_customer
from .views import customer_list
from .views import customer_details_view



urlpatterns = [
    path("customer/upload/", upload_customer, name= "upload_customer"),
    path("customer/list/", customer_list, name= "customer_list"),
    path("customer/<int:id>/",customer_details_view,name="customer_details_view")
]
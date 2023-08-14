from django.urls import path 
from .views import upload_cart
from .views import cart_list
from .views import cart_details_view
# urlpatterns = [
#     path("customer/upload/", upload_customer, name= "upload_customer"),
# ]

urlpatterns = [
    path("cart/upload/", upload_cart, name= "upload_cart_"),
    path("cart/list/", cart_list, name= "cart_list"),
    path("cart/<int:id>/",cart_details_view,name="cart_details_view")
]
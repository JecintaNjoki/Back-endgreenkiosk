from django.urls import path 
from .views import upload_cart
from .views import cart_list
from .views import cart_details_view
# urlpatterns = [
#     path("customer/upload/", upload_customer, name= "upload_customer"),
# ]

urlpatterns = [
    path("cart_/upload/", upload_cart, name= "upload_cart_"),
    path("cart_/list/", cart_list, name= "cart__list"),
    path("cart_/<int:id>/",cart_details_view,name="cart__details_view")
]
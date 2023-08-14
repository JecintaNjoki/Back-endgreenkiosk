from django.urls import path 
from .views import upload_order
from .views import order_list
from .views import order_details_view


urlpatterns = [
    path("order_/upload/", upload_order, name= "upload_order"),
    path("order_/list/", order_list, name= "order__list"),
    path("order_/<int:id>/",order_details_view,name="order__details_view")
]
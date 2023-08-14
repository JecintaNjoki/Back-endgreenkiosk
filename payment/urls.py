from django.urls import path 
from .views import upload_payment
from .views import payment_list
from .views import payment_details_view


urlpatterns = [
    path("payment_/upload/", upload_payment, name= "upload_payment"),
    path("payment_/list/", payment_list, name= "payment__list"),
    path("payment_/<int:id>/",payment_details_view,name="payment_details_view")
]
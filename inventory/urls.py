from django.urls import path 
from .views import upload_product
from .views import products_list

urlpatterns = [
    path("products/upload/", upload_product, name= "upload_product"),
    path("products/list/", products_list, name= "product_list"),
    path("products/<int:id>/",products_details_view,name="products_details_view")
]

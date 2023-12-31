from django.urls import path 
from .views import upload_product
from .views import products_list
from .views import products_details_view
from .views import edit_product_view

urlpatterns = [
    path("products/upload/", upload_product, name= "upload_product"),
    path("products/list/", products_list, name= "product_list"),
    path("products/details/<int:id>/",products_details_view,name="products_details_view"),
    path("products/edit/<int:id>/", edit_product_view, name='edit_product_view')
]

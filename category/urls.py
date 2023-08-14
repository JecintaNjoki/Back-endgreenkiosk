from django.urls import path 
from .views import upload_category
from .views import category_list
from .views import category_details_view
# urlpatterns = [
#     path("customer/upload/", upload_customer, name= "upload_customer"),
# ]

urlpatterns = [
    path("category_/upload/", upload_category, name= "upload_category_"),
    path("category_/list/", category_list, name= "category__list"),
    path("category_/<int:id>/",category_details_view,name="category__details_view")
]





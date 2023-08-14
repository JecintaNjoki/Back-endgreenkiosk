from django.shortcuts import render

# Create your views here.

from .forms import CartUploadForm
from cart.models import Cart

def upload_cart(request):
    if request.method == "POST":
        form = CartUploadForm(request.POST,request.Files)
        if form.isvalid():
            form.save()
    else:
        form = CartUploadForm()
    return render(request,"cart/cart_upload.html",{"form":form})

def cart_list(request):
    carts= Cart.objects.all()
    return render(request, 'cart/cart_list.html', {'carts': carts})

def cart_details_view(request,id):
    cart=Cart.objects.get(id=id)
    return render(request, 'cart/cart_details.html', {'cart': cart})
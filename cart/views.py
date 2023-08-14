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
    return render(request,"Cart/cart_upload.html",{"form":form})

def cart_list(request):
    cart= Cart.objects.all()
    return render(request, 'Cart/cart_list.html', {'cart': cart})

def cart_details_view(request,id):
    cart=Cart.objects.get(id=id)
    return render(request, 'Cart/cart_details.html', {'cart': cart})
from django.shortcuts import render

# Create your views here.

from .forms import CartUploadForm
from .forms import Cart

def upload_cart(request):
    cart = CartUploadForm()
    return render(request, 'Cart/cart_upload.html', {'cart': cart})

def products_list(request):
    cart= Cart.objects.all()
    return render(request, 'Cart/cart_list.html', {'cart': cart})

def products_details_view(request,id):
    cart=Cart.objects.get(id=id)
    return render(request, 'Cart/cart_details.html', {'cart': cart})
from django.shortcuts import render

# Create your views here.
from .forms import ProductUploadForm
from .forms import Products

def upload_product(request):
    form = ProductUploadForm()
    return render(request, 'inventory/product_upload.html', {'form': form})

def products_list(request):
    products= Products.objects.all()
    return render(request, 'inventory/product_list.html', {'products': products})

def products_details_view(request,id):
    products=Products.objects.get(id=id)
    return render(request, 'inventory/products_details.html', {'products': products})









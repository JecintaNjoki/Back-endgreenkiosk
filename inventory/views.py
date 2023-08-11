from django.shortcuts import render

# Create your views here.
from .forms import ProductUploadForm

def upload_product(request):
    form = ProductUploadForm()
    return render(request, 'inventory/product_upload.html', {'form': form})

def products_list(request):
    products= products.objects.all()
    return render(request, 'inventory/product_list.html', {'products': products})

def products_details_view(request,id):
    products=products.objects.get(id=id)
    return render(request, 'inventory/products_details.html', {'products': products})









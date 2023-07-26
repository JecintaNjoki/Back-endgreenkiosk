from django.shortcuts import render

# Create your views here.
from .forms import ProductUploadForm
def upload_product(request):
    form = ProductUploadForm()
    return render(request, 'inventory/product_upload.html', {'form': form})
from django.shortcuts import render

# Create your views here.
from.forms import CustomerUploadForm
def upload_customer(request):
    form = CustomerUploadForm()
    return render(request, 'Customer/customer_upload.html', {'form': form})
from django.shortcuts import render

# Create your views here.
from.forms import CustomerUploadForm
def upload_customer(request):
    form = CustomerUploadForm()
    return render(request, 'Customer/customer_upload.html', {'form': form})

def customer_list(request,id):
    customer=customer.objects.get(id=id)
    return render(request, 'Customer/customer_list.html', {'customer': customer})

def customer_details_view(request,id):
 customer = customer.objects.get(id=id)
 return render(request, 'Customer/customer_details.html', {'customer': customer})






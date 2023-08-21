from django.shortcuts import render

# Create your views here.
from vendor.forms import VendorUploadForm
from customer.models import Vendor

def upload_vendor(request):
    if request.method == "POST":
        form = VendorUploadForm(request.POST,request.Files)
        if form.isvalid():
            form.save()
    else:
        form = VendorUploadForm()
    return render(request,"Vendor/vendor_upload.html",{"form":form})

def vendor_list(request,id):
    vendor=Vendor.objects.get(id=id)
    return render(request, 'vendor/vendor_list.html', {'vendor': vendor})

def vendor_details_view(request,id):
    vendor = Vendor.objects.get(id=id)
    return render(request, 'vendor/vendor_details.html', {'vendor': vendor})



from django.shortcuts import render

# Create your views here.

from .forms import OrderUploadForm
from order.models import Order

def upload_order(request):
    if request.method == "POST":
        form = OrderUploadForm(request.POST,request.Files)
        if form.isvalid():
            form.save()
    else:
        form = OrderUploadForm()
    return render(request,"Order/order_upload.html",{"form":form})

def order_list(request):
    order= Order.objects.all()
    return render(request, 'Order/order_list.html', {'order': order})

def order_details_view(request,id):
    order=Order.objects.get(id=id)
    return render(request, 'Order/order_details.html', {'order': order})
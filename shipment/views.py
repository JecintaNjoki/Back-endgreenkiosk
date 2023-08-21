from django.shortcuts import render, redirect
from .forms import ShipmentUploadForm
from .models import Shipment

# Create your views here.
def upload_shipment(request):
    if request.method == "POST":
        form = ShipmentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ShipmentUploadForm()
    return render(request, "shipment/shipment_upload.html", {"form": form})

def shipment_list(request):
    shipment = Shipment.objects.all()
    return render(request, "shipment/shipment_list.html", {"shipment": shipment})

def shipment_details(request, id):
    shipment = Shipment.objects.get(id=id)
    return render(request, "shipment/shipment_detail.html", {"shipment": shipment})

def edit_shipment_view(request, id):
    shipment = Shipment.objects.get(id=id)
    if request.method == "POST":
        form = ShipmentUploadForm(request.POST, instance=shipment)
        if form.is_valid():
            form.save()
            return redirect("shipment_detail_view", id=shipment.id)
    else:
        form = ShipmentUploadForm(instance=shipment)
    return render(request, "shipment/edit_shipment.html", {"form": form})



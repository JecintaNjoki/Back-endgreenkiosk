from django.shortcuts import render

# Create your views here.
from .forms import PaymentUploadForm
from payment.models import Payment


def upload_payment(request):
    if request.method == "POST":
        form = PaymentUploadForm(request.POST,request.Files)
        if form.isvalid():
            form.save()
    else:
        form = PaymentUploadForm()
    return render(request,"payment/payment_upload.html",{"form":form})

def payment_list(request):
    payment= Payment.objects.all()
    return render(request, 'payment/payment_list.html', {'payment': payment})

def payment_details_view(request,id):
    payment=Payment.objects.get(id=id)
    return render(request, 'payment/payment_details.html', {'payment': payment})
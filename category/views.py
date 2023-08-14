from django.shortcuts import render

# Create your views here.

from .forms import CategoryUploadForm
from category.models import Category

def upload_category(request):
    if request.method == "POST":
        form = CategoryUploadForm(request.POST,request.Files)
        if form.isvalid():
            form.save()
    else:
        form = CategoryUploadForm()
    return render(request,"Category/category_upload.html",{"form":form})

def category_list(request):
   category= Category.objects.all()
   return render(request, 'Category/category_list.html', {'category': category})

def category_details_view(request,id):
    category=Category.objects.get(id=id)
    return render(request, 'Category/category_details.html', {'category': category})
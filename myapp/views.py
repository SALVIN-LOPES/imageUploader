from django.shortcuts import render
from django.http import HttpResponse
from myapp.forms import ImageForm
from .models import Image

def home(request):
    form = ImageForm()
    if request.method == 'POST':
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    
    images = Image.objects.all()

    context = {
        'form' : form,
        'images' : images
    }
    return render(request,"myapp/home.html",context)

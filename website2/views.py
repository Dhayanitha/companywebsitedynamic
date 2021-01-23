from django.shortcuts import render
from .models import People
from .models import Product
# Create your views here.
def home(request):
    context = {}
    return render(request, 'website2/home.html', context)

def product(request):
    context = {}
    context['products'] = Product.objects.all()
    return render(request, 'website2/products.html',context)
   
def people(request):
    context = {}
    context['peoples'] = People.objects.all()
    return render(request, 'website2/people.html', context)  

def contact(request):
    context = {}
    return render(request, 'website2/contact.html', context)

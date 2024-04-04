from django.shortcuts import render
from .models import Product
# Create your views here.

products = Product.objects.all()
def index(request):
    return render(request, 'index.html',
                  {'products':products})



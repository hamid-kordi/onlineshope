from django.shortcuts import render,redirect
from django.views import View
from .models import Product,Category
from django.shortcuts import get_object_or_404
# Create your views here.


class HomeVeiw(View):

    def get(self,request):
        products = Product.objects.filter(available=True)
        return render(request,'home/home.html',{'products':products})

class ProductDetailView(View):
    
    def get(self,request,slug):
        product = get_object_or_404(Product,slug=slug)
        return render(request,'home/details.html',{'product':product})
        
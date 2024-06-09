from django.shortcuts import render,redirect
from django.views import View
from .models import Product,Category
from django.shortcuts import get_object_or_404
from .tasks import all_bucket_object_task
# Create your views here.


class HomeVeiw(View):

    def get(self,request):
        products = Product.objects.filter(available=True)
        return render(request,'home/home.html',{'products':products})

class ProductDetailView(View):
    
    def get(self,request,slug):
        product = get_object_or_404(Product,slug=slug)
        return render(request,'home/details.html',{'product':product})
        

class BucketHome(View):
    template_name = 'home/bucket.html'
    def get(self,request):
        objects = all_bucket_object_task()
        print(objects)
        return render(request,'home/bucket.html',{'objects':objects})
        
    
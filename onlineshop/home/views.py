from django.shortcuts import render, redirect
from django.views import View
from .models import Product, Category
from django.shortcuts import get_object_or_404
from . import tasks
from django.contrib import messages
from utils import IsAdminUserMixin
from orders.forms import CartAddForm

# Create your views here.


class HomeVeiw(View):

    def get(self, request, category_slug=None):
        products = Product.objects.filter(available=True)
        categoris = Category.objects.filter(is_sub=False)
        if category_slug:

            category = Category.objects.get(slug=category_slug)
            products = products.filter(category=category)
        return render(
            request, "home/home.html", {"products": products, "categoris": categoris}
        )


class ProductDetailView(View):
    form_class = CartAddForm

    def get(self, request, slug):
        form = self.form_class
        product = get_object_or_404(Product, slug=slug)
        return render(request, "home/details.html", {"product": product, "form": form})


class BucketHome(IsAdminUserMixin, View):
    template_name = "home/bucket.html"

    def get(self, request):
        objects = tasks.all_bucket_object_task()
        print(objects)
        return render(request, "home/bucket.html", {"objects": objects})


class DeleteObjectBucketView(IsAdminUserMixin, View):
    def get(self, request, key):
        tasks.delete_object_task.delay(key)
        messages.success(request, "will done very soon", "info")
        return redirect("home:bucket")


class DownloadObjectBucketView(IsAdminUserMixin, View):
    def get(self, request, key):
        tasks.download_object_bucket_task.delay(key)
        messages.success(request, "will download very soon", "info")
        return redirect("home:bucket")

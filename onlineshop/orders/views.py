from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .carts import Cart
from home.models import Product
from .forms import CartAddForm

# Create your views here.


class HomeViewOrder(View):
    def get(self, request):
        cart = Cart(request)
        return render(request, "orders/cart.html", {"cart": cart})


class HomeViewCart(View):
    def post(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        form = CartAddForm(request.POST)
        if form.is_valid():
            cart.add(product, form.cleaned_data["quantity"])
        return redirect("orders:cart")

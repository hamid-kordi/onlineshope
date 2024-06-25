from django.urls import path
from . import views

app_name = "orders"
urlpatterns = [
    path("create/", views.OrderCreateView.as_view(), name="order_create"),
    path(
        "detail/<int:order_id>/", views.OrderDetailView.as_view(), name="order_detail"
    ),
    path("cart/", views.HomeViewOrder.as_view(), name="cart"),
    path("cart/add/<int:product_id>/", views.HomeViewCart.as_view(), name="cart_add"),
    path(
        "cart/delete/<int:product_id>/",
        views.DeleteViewCart.as_view(),
        name="delete_cart",
    ),
    path("apply/<int:order_id>/", views.CouponApplyView.as_view(), name="copunapply"),
]

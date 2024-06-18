from django.urls import path
from . import views

app_name = "orders"
urlpatterns = [path("card/", views.HomeViewOrder.as_view(), name="orders")]

from django.conf.urls import url
from . import views

app_name = "reports"

urlpatterns = [
	url(r'^', views.cart_view, name="cart_view"),
]
from django.conf.urls import url
from . import views

app_name = "reports"

urlpatterns = [
	url(r'^(?P<user_id>[0-9]+)', views.cart_view, name="cart_view"),
]
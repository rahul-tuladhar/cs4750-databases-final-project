from django.conf.urls import url 
from . import views

app_name = "create"

urlpatterns = [
	url(r'^product/$', views.product_view, name='productview'),
]
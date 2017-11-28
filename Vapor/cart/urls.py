from django.conf.urls import url
from . import views

app_name = "reports"

urlpatterns = [
	url(r'', views.defaultCart, name="defaultCart"),
]
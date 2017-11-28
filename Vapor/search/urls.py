from django.conf.urls import url 
from . import views

app_name = "search"

urlpatterns = [
	url(r'^product/(?P<product_id>[0-9]+)', views.detail_view, name='detailview'),
	url(r'^results$', views.results_view, name='resultsview'),
	url(r'', views.search_view, name='searchview'),
]
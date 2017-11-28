	
from django.conf.urls import url, include
from django.contrib import admin
from . import views

#Add Django site authentication urls (for login, logout, password management)
urlpatterns = [
    url(r'^accounts/', include('django.contrib.auth.urls')), 	
   	url(r'^register/$', views.register_user, name='register-user'),
    url(r'^confirm/(?P<activation_key>\w+)/$', views.register_confirm, name='register-confirm'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),

]

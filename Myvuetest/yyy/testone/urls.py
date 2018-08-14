from django.conf.urls import url
from testone import views

 
urlpatterns = [
    url(r'^$', views.login),
    url(r'^login/$', views.login),
    url(r'^regist/$', views.regist),
    url(r'^index/$', views.index),
    url(r'^logout/$', views.logout),
    url(r'^edit/$', views.useredit),
    url(r'^delete/$', views.delete)
]
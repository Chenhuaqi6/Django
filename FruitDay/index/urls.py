from django.conf.urls import url
from . import views

urlpatterns = [
    #匹配首页
    url(r'^$',views.index),
    url(r'^cart/$',views.cart),
    url(r'^register/$',views.register),
    url(r'^login/$',views.modellogin),

]
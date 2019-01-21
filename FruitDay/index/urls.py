from django.conf.urls import url
from . import views

urlpatterns = [
    #匹配首页
    url(r'^$',views.index),
    url(r'^cart/$',views.cart),
    url(r'^register/$',views.register),
    url(r'^login/$',views.modellogin),
    #查询数据库是否存在该手机号
    url(r'^check_phone/$',views.check_phone),
    #匹配 check_login/
    url(r'^check_login/$',views.check_login),
    #匹配 type_goods/
    url(r'^type_goods/$',views.type_goods),


]
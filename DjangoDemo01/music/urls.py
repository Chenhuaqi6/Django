from django.conf.urls import url
from . import views

urlpatterns = [

    # url(r'^index/$',views.show)
    #当访问路径是 空的时候
    url(r'^$',views.index),


    #访问路径:01-template/ 交给template_views()处理
    url(r'^01-template/$',views.template_views),

    #访问路径:02-var/ 交给var_views()处理
    url(r'^02-var/$',views.var_views),
    #访问路径: 03-static/ 交给static_views()处理
    url(r'^03-static/',views.static_views),
    #访问路径:04-parent/ 交给
    url(r'^04-parent/$',views.parent),

    url(r'^05-child/$',views.child),
    #访问路径:06-thisisatest_user_login_path
    url(r'^06-thisisatest_user_login_path/$',views.test_views,name='log'),

    url(r'^07-thisisanother_user_register/(\d{4})/$',views.reg_views,name='reg'),
]


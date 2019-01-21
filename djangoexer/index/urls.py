from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^00-post/$',views.register_views),
    url(r'^01-login/$',views.login_views),
    url(r'^02-widget01/$',views.widget01),
    url(r'^03-setcookie/$',views.set_cookie),
    url(r'^04-getcookie/$',views.get_cookie),
    url(r'^05-setsession/$',views.set_session),
    url(r'^06-getsession/$',views.get_session),
]

#Django中ajax的处理路由
urlpatterns +=[
    url(r'^07-ajax-get/$',views.ajax_get),
    url(r'^08-ajax-params/$',views.ajax_params),
    url(r'^13-ajax-post/$',views.ajax_post),
    url(r'^14-ajax-json/$',views.ajax_json),
]
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^01-add-author/$',views.add_author),
    url(r'^02-add-book/$',views.add_book),
    url(r'^03-add-publisher/$',views.add_publisher),
    url(r'^04-query/$',views.query),
    url(r'^03-queryall/$',views.queryall),
    url(r'^04-filter/$',views.filter_query),
    url(r'^05-filter-aa/$',views.filter_aa),
    url(r'^05-update/(\d+)/$',views.update),
    url(r'^06-aggregate/$',views.aggregate),
    url(r'^07-annotate/$',views.annotate),
    url(r'^07-exercise/$',views.exercise),
    url(r'^08-update/$',views.update08),
    url(r'^09-delete/(\d+)/$',views.delete),

]

urlpatterns +=[
    url(r'^10-oto/$',views.oto_views),
    url(r'^11-omany/$',views.onemany),
    url(r'^12-mtm/$',views.mtm_views),
    url(r'^13-objects/$',views.objects_views),
]
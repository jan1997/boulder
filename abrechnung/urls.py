from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^abrechnungen/$', views.rechnung_list, name='rechnung_list'),
    url(r'^rechnung/new/$', views.rechnung_new, name='rechnung_new'),
    url(r'^rechnung/delete/(?P<pk>\d+)/$', views.rechnung_delete, name='rechnung_delete'),
]
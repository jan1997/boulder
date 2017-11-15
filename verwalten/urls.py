from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^users/$', views.user_list, name='user_list'),
    url(r'^user/(?P<pk>\d+)/$', views.user_detail, name='user_detail'),
    url(r'^user/new/$', views.user_new, name='user_new'),
]
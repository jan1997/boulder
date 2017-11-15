from django.conf.urls import include
from django.contrib import admin
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from verwalten import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'', include('verwalten.urls')),
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^accounts/profile/$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^blog/', include('blog.urls')),
    url(r'^abrechnung/', include('abrechnung.urls')),
]
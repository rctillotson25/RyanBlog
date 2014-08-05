from django.conf.urls import patterns, url

from Blog import views

urlpatterns = patterns ('',
	url(r'^$', views.index, name='index'),
	url(r'^(?P<post_id>\d+)/$', views.detail, name='detail'),
	url(r'^(?P<post_id>\d+)/results/$', views.results, name='results'),
	url(r'^(?P<post_id>\d+)/check/$', views.check, name='check'),
)



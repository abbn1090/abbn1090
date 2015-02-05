from django.conf.urls import patterns, url
from . import views, feed
urlpatterns = patterns(
'',
url(r'^feed/$', feed.LatestPosts(), name="feed"),
url(r'^$', views.BlogIndex.as_view(), name="index"),#as_view():Returns a callable view that takes a request and returns a response
url(r'^entry/(?P<slug>\S+)$', views.BlogDetail.as_view(), name="entry_detail"),
#url(r'^pics/(?P<path>.*)$', 'django.views.static.serve',
 #                {'document_root': settings.MEDIA_ROOT}),
)

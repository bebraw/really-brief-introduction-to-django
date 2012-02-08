from django.conf.urls.defaults import patterns
import views

urlpatterns = patterns('',
    (r'^hello/$', views.hello),
    (r'^hello/(?P<id>\d+)/$', views.hello2)
)


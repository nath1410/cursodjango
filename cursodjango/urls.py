from django.conf.urls import patterns, include, url
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'aula6.views.index'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^aula3/$', 'aula3.views.index', name='aula3_index'),
    url(r'^aula3/(?P<username>[\w-]+)/$', 'aula3.views.detail', name='aula3_detail'),
    url(r'^aula4/$', 'aula4.views.index', name='aula4_index'),
    url(r'^aula4/home/$', 'aula4.views.home', name='aula4_home'),
    url(r'^aula6/$', 'aula6.views.index', name='aula6_index'),
)

if settings.DEBUG:
	urlpatterns += patterns('',
		(r'^media/(?P<path>.*)$', 'django.views.static.serve',
			{'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
	)

#	urlpatterns += staticfiles_urlpatterns
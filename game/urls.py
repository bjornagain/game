from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'main.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^name/', 'main.views.name'),
    url(r'^actions/', 'main.views.actions'),
    url(r'^accounts/login/$', 'main.views.login'),
    url(r'^accounts/auth/$', 'main.views.auth_view'),
    url(r'^accounts/logout/$', 'main.views.logout'),
    url(r'^accounts/loggedin/$', 'main.views.loggedin'),
    url(r'^accounts/invalid/$', 'main.views.invalid_login'),
    url(r'^accounts/register/$', 'main.views.register_user'),
    url(r'^accounts/register_success/$', 'main.views.register_success'),
    url(r'^test/', 'main.views.test'),
    url(r'^static/(?P<path>.*)$','django.views.static.serve'),
	(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    

    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

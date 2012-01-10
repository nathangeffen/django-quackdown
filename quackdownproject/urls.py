from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from quackdown.feeds import LatestClaimsAndResponsesAtomFeed,\
    LatestClaimsAndResponsesRSSFeed

admin.autodiscover()

urlpatterns = patterns('',
    (r'^', include('pubman.urls')),    
    (r'^quackdown/', include('quackdown.urls')),
    (r'^grappelli/', include('grappelli.urls')),
    (r'^admin/filebrowser/', include('filebrowser.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    
    url(r'^feed/rss/claimsandresponses/$', LatestClaimsAndResponsesRSSFeed(), name='rss-feed-claims-responses'),
    url(r'^feed/atom/claimsandresponses/$', LatestClaimsAndResponsesAtomFeed(), name='atom-feed-claims-responses'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^' + settings.MEDIA_URL[1:] + r'(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    )

urlpatterns += staticfiles_urlpatterns()

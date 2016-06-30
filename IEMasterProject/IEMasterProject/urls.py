from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
import IEMasterProject.views as views
from django.conf import settings

urlpatterns = [

    # Examples:
    # url(r'^$', 'IEMasterProject.views.home', name='home'),
    # url(r'^IEMasterProject/', include('IEMasterProject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', views.homePage, name='homePage'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^exiovisuals/', include('ExioVisuals.urls')),
    url(r'^puma/', include('PUMA.urls')),
    url(r'^EFactor/', include('EFactor.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    url(r'^about/', views.about, name='about'),

    ]

    #url(r'^PUMA/', include('PUMA.urls'),)))

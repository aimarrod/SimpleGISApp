from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^routes/$', 'routes.views.route'),
    (r'^ajax/(?P<pk>\d+)/route/$', 'routes.views.routeJSON'),

    
)

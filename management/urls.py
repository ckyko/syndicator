from django.conf.urls import url, include

from . import views
urlpatterns = [

    url(r'run$', views.index, name='index'),
    url(r'check_eventbrite_events$', views.eventbrite_events, name='events'),


]
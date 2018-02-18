from django.conf.urls import url, include

from . import views
urlpatterns = [

    url(r'run$', views.index, name='index'),
    url(r'check_eventbrite_events$', views.eventbrite_events, name='events'),
    url(r'test_tl$', views.test_tl, name='test_tl'),
    url(r'test_tb$', views.test_tb, name='test_TicketbudPoster'),
    url(r'test_eventful$', views.test_eventful, name='test_Eventful'),


]
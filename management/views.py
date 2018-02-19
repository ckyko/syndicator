import requests

from django.conf import settings
from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

from .cron import MyCronJob
from .poster import TicketleapPoster, TicketbudPoster, EventfulPoster


# Create your views here.
def run(request):
    cron_job = MyCronJob()
    cron_job.do()
    return HttpResponse("Finished.")


@login_required
def eventbrite_events(request):
    url = "https://www.eventbriteapi.com/v3/users/me/owned_events/?token=" + settings.EVENTBRITE_TOKEN
    response = requests.get(url=url, verify=True)

    return HttpResponse(str(response.json()))


@login_required
def test_tl(request):
    ticketleap_poster = TicketleapPoster()
    ticketleap_poster.post_product("fake_product_for_testing")

    return HttpResponse("Finish test.")

@login_required
def test_tb(request):
    tb_poster = TicketbudPoster()
    tb_poster.post_product("fake_product_for_testing")

    return HttpResponse("Finish test.")

@login_required
def test_eventful(request):
    tb_poster = EventfulPoster()
    tb_poster.post_product("fake_product_for_testing")

    return HttpResponse("Finish test.")

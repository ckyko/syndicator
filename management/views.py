import requests

from django.conf import settings
from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

from .cron import MyCronJob


# Create your views here.
def index(request):
    cron_job = MyCronJob()
    cron_job.do()
    return HttpResponse("Finished.")


@login_required
def eventbrite_events(request):
    url = "https://www.eventbriteapi.com/v3/users/me/owned_events/?token=" + settings.EVENTBRITE_TOKEN

    response = requests.get(url=url, verify=True)
    print(response.json())
    print(response.status_code)

    return HttpResponse(str(response.json()))

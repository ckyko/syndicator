from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

from .cron import MyCronJob


# Create your views here.
@login_required
def index(request):
    print("get in index")
    cron_job = MyCronJob()
    cron_job.do()
    return HttpResponse("success.")

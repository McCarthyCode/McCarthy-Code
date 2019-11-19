import pytz

from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponseBadRequest
from mwd.settings import TIME_ZONE

TITLE = 'McCarthy Web Design'

def index(request):
    if request.method != 'GET':
        return HttpResponseBadRequest()

    return render(request, 'home/index.html', {
        'title': TITLE,
        'year': datetime.now(pytz.timezone(TIME_ZONE)).year,
    })
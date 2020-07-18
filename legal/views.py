import pytz

from datetime import datetime

from django.shortcuts import render
from mwd.settings import STAGE, TIME_ZONE

def index(request):
    if request.method != 'GET':
        return HttpResponseBadRequest()

    return render(request, 'legal/index.html', {
        'stage': STAGE,
        'year': datetime.now(pytz.timezone(TIME_ZONE)).year,
    })

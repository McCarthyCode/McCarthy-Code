import pytz

from datetime import datetime

from django.contrib import messages
from django.http import HttpResponseBadRequest, HttpResponseForbidden
from django.shortcuts import render, redirect

from .forms import SiteForm
from .models import Site, Screenshot
from mwd.settings import TIME_ZONE

TITLE = 'McCarthy Web Design'

def index(request):
    if request.method != 'GET':
        return HttpResponseBadRequest()

    return render(request, 'home/index.html', {
        'title': TITLE,
        'year': datetime.now(pytz.timezone(TIME_ZONE)).year,
    })

def portfolio(request):
    if request.method != 'GET':
        return HttpResponseBadRequest()

    sites = []
    for site in Site.objects.all().order_by('date_created'):
        sites.append({
            'data': site,
            'screenshots': Screenshot.objects.filter(site=site).order_by('-date_updated'),
        })

    return render(request, 'home/portfolio.html', {
        'sites': sites,
        'title': TITLE,
        'year': datetime.now(pytz.timezone(TIME_ZONE)).year,
    })

def add_site(request):
    # if not request.user.is_superuser:
    #     return HttpResponseForbidden()

    if request.method == 'GET':
        return render(request, 'home/add_site.html', {
            'form': SiteForm(),
            'title': TITLE,
            'year': datetime.now(pytz.timezone(TIME_ZONE)).year,
        })
    elif request.method == 'POST':
        form = SiteForm(request.POST, request.FILES)

        if form.is_valid():
            site = form.save()

            for image in request.FILES.getlist('screenshots'):
                screenshot = Screenshot.create(image=image, site=site)
                screenshot.save()

            messages.success(request, 'You have successfully added "%s."' % site.name)

            return redirect('home:add-site')

        messages.error(request, 'There was an error adding a site.')

        return redirect('home:add-site')

    return HttpResponseBadRequest()

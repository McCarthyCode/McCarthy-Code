import json
import pytz

from datetime import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import (
    HttpResponseBadRequest,
    HttpResponseForbidden,
    HttpResponseRedirect,
)
from django.shortcuts import render, redirect, reverse, get_object_or_404

from .forms import SiteForm
from .models import Site, Screenshot
from mwd.settings import STAGE, TIME_ZONE

def view_400(request, exception=None):
    return render(request, 'home/errors/400.html', status=200)

def view_403(request, exception=None):
    return render(request, 'home/errors/403.html', status=200)

def view_404(request, exception=None):
    return render(request, 'home/errors/404.html', status=200)

def view_500(request, exception=None):
    return render(request, 'home/errors/500.html', status=200)

def index(request):
    if request.method != 'GET':
        return HttpResponseBadRequest()

    return render(request, 'home/index.html', {
        'stage': STAGE,
        'year': datetime.now(pytz.timezone(TIME_ZONE)).year,
    })

def legal(request):
    if request.method != 'GET':
        return HttpResponseBadRequest()

    return render(request, 'legal/index.html', {
        'stage': STAGE,
        'year': datetime.now(pytz.timezone(TIME_ZONE)).year,
    })

def login_view(request):
    if request.method == 'GET':
        return render(request, 'home/login.html', {
            'stage': STAGE,
            'year': datetime.now(pytz.timezone(TIME_ZONE)).year,
        })
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)

            messages.success(request, 'Welcome, %s!' %
                (user.first_name if user.first_name else user.username)
            )

            return redirect('home:sites')
        else:
            messages.error(request, 'There was an error logging in with that username/password combination.')

            return redirect('home:login')
    else:
        return HttpResponseBadRequest()

def logout_view(request):
    if request.method != 'GET':
        return HttpResponseBadRequest()

    logout(request)

    messages.success(request, 'You have successfully logged out.')

    return redirect('home:login')

def portfolio(request):
    if request.method != 'GET':
        return HttpResponseBadRequest()

    sites = []
    for site in Site.objects.all().order_by('-date_updated'):
        sites.append({
            'data': site,
            'screenshots': Screenshot.objects.filter(site=site).order_by('date_updated'),
        })

    return render(request, 'home/portfolio.html', {
        'sites': sites,
        'stage': STAGE,
        'year': datetime.now(pytz.timezone(TIME_ZONE)).year,
    })

def about(request):
    if request.method != 'GET':
        return HttpResponseBadRequest()

    return render(request, 'home/about.html', {
        'stage': STAGE,
        'year': datetime.now(pytz.timezone(TIME_ZONE)).year,
    })

def sites(request):
    if request.method != 'GET':
        return HttpResponseBadRequest()

    sites = []
    for site in Site.objects.all().order_by('-date_updated'):
        sites.append({
            'data': site,
            'screenshots': Screenshot.objects.filter(site=site).order_by('date_updated')[:3],
        })

    return render(request, 'home/sites.html', {
        'sites': sites,
        'stage': STAGE,
        'year': datetime.now(pytz.timezone(TIME_ZONE)).year,
    })

def add_site(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden()

    if request.method == 'GET':
        return render(request, 'home/add_site.html', {
            'form': SiteForm(),
            'stage': STAGE,
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

            return redirect('home:sites')

        messages.error(request, 'There was an error adding a site.')

        return redirect('home:add-site')

    return HttpResponseBadRequest()

def edit_site(request, site_id):
    if not request.user.is_superuser:
        return HttpResponseForbidden()

    site = get_object_or_404(Site, id=site_id)

    if request.method == 'GET':
        return render(request, 'home/edit_site.html', {
            'site': site,
            'screenshots': Screenshot.objects.filter(site=site).order_by('date_updated'),
            'form': SiteForm(instance=site),
            'stage': STAGE,
            'year': datetime.now(pytz.timezone(TIME_ZONE)).year,
        })
    elif request.method == 'POST':
        form = SiteForm(request.POST, request.FILES, instance=site)

        if form.is_valid():
            site = form.save()

            order = json.loads(request.POST.get('order'))

            for screenshot_id in order:
                screenshot = get_object_or_404(Screenshot, id=screenshot_id)
                screenshot.save()

            for image in request.FILES.getlist('screenshots'):
                screenshot = Screenshot.create(image=image, site=site)
                screenshot.save()

            messages.success(request, 'You have successfully edited "%s."' % site.name)

            return redirect('home:sites')

        messages.error(request, 'There was an error editing the site.')

        return HttpResponseRedirect(
            reverse('home:edit-site', args=[site_id])
        )

    return HttpResponseBadRequest()

def delete_site(request, site_id):
    if request.method != 'GET':
        return HttpResponseBadRequest()

    site = get_object_or_404(Site, id=site_id)
    site.delete()

    messages.success(request, 'You have successfully deleted "%s" and its corresponding screenshots.' % site.name)

    return redirect('home:sites')

def delete_screenshot(request, site_id, screenshot_id):
    if request.method != 'GET':
        return HttpResponseBadRequest()

    site = get_object_or_404(Site, id=site_id)
    screenshot = get_object_or_404(Screenshot, id=screenshot_id)

    assert site == screenshot.site

    screenshot.delete()

    messages.success(request, 'Screenshot successfully deleted.')

    return HttpResponseRedirect(
        reverse('home:edit-site', args=[site_id])
    )

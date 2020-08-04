import json

from django.contrib import messages
from django.http import (
    HttpResponseBadRequest,
)
from django.shortcuts import render, redirect

from .forms import QuoteRequestForm
from home.recaptcha import get_client_ip, verify

def index(request):
    if request.method == 'GET':
        return render(request, 'quotes/index.html', {
            'form': QuoteRequestForm(),
        })
    elif request.method == 'POST':
        form = QuoteRequestForm(request.POST)

        g_recaptcha_response = request.POST.get('g-recaptcha-response')
        ip = get_client_ip(request)

        api_response = verify(g_recaptcha_response, ip)
        api_response_content = json.loads(str(api_response.content, encoding='utf-8'))

        if not api_response_content['success'] or api_response.status_code != 200:
            messages.error(request, 'There was an error submitting the form.')
            messages.error(request, 'Please prove you are human by checking the checkbox labeled "I\'m not a robot" and possibly completing a security challenge.')

            return render(request, 'quotes/index.html', {'form': form})

        if form.is_valid():
            quote_request = form.save(commit=False)

            quote_request.contact = form.cleaned_data['contact']
            quote_request.save()

            messages.success(request, 'Thank you for submitting a quote request. McCarthy Web Design will contact you via phone or email within 1-3 business days.')

            return redirect('quotes:index')

        messages.error(request, 'There was an error submitting the form.')

        return render(request, 'quotes/index.html', {
            'form': form,
        })

    return HttpResponseBadRequest()

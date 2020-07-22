from django.contrib import messages
from django.http import (
    HttpResponseBadRequest,
)
from django.shortcuts import render, redirect

from .forms import QuoteRequestForm

def index(request):
    if request.method == 'GET':
        return render(request, 'quotes/index.html', {
            'form': QuoteRequestForm(),
        })
    elif request.method == 'POST':
        form = QuoteRequestForm(request.POST)

        if form.is_valid():
            quote_request = form.save()

            messages.success(request, 'Thank you for submitting a quote request. McCarthy Web Design will contact you via phone or email within 1-3 business days.')

            return redirect('quotes:index')

        messages.error(request, 'There was an error submitting the form.')

        return render(request, 'quotes/index.html', {
            'form': form,
        })

    return HttpResponseBadRequest()

import requests

from mwd.settings import RECAPTCHA_V2_SECRET_KEY, RECAPTCHA_V3_SECRET_KEY

def _get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    return ip

def verify_v2(request):
    return requests.post('https://www.google.com/recaptcha/api/siteverify', {
        'secret': RECAPTCHA_V2_SECRET_KEY,
        'response': request.POST.get('g-recaptcha-response'),
        'remoteip': _get_client_ip(request),
    })

def verify_v3(request):
    return requests.post('https://www.google.com/recaptcha/api/siteverify', {
        'secret': RECAPTCHA_V3_SECRET_KEY,
        'response': request.POST.get('g-recaptcha-response'),
        'remoteip': _get_client_ip(request),
    })

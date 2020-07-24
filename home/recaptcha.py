import requests

from mwd.settings import RECAPTCHA_SECRET_KEY

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    return ip

def verify(response, ip):
    return requests.post('https://www.google.com/recaptcha/api/siteverify', {
        'secret': RECAPTCHA_SECRET_KEY,
        'response': response,
        'remoteip': ip,
    })

import pytz

from datetime import datetime

from mwd.settings import STAGE, TIME_ZONE

def stage(request):
    return {'stage': STAGE}

def year(request):
    return {'year': datetime.now(pytz.timezone(TIME_ZONE)).year}

def recaptcha_site_key(request):
    return {'recaptcha_site_key': '6LcM4LQZAAAAAOXJ-CSlz-JrFWKSEl6zfOBmB4Hg'}

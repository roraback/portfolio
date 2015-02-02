from django.conf import settings

def portfolio_settings(request):
    return {
        'ENVIRONMENT': settings.ENVIRONMENT,
        'DEBUG': settings.DEBUG,
    }

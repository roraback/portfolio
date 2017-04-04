from django.conf import settings
from django.http import HttpResponsePermanentRedirect


class EnsureHttpsMiddleware(object):

    def process_request(self, request):
        if not settings.DEBUG and not request.is_secure():
            url_str = request.build_absolute_uri()
            url_str = url_str.replace('http://', 'https://')
            return HttpResponsePermanentRedirect(url_str)
        return None
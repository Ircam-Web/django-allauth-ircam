from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns,url
from .provider import IrcamAuthProvider
from django.conf import settings

if getattr(settings, 'OAUTH2_IRCAM', False):
    if settings.OAUTH2_IRCAM:
        urlpatterns = default_urlpatterns(IrcamAuthProvider)
else:
    urlpatterns = default_urlpatterns(IrcamAuthProvider)

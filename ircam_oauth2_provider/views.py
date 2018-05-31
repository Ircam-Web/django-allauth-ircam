import requests
from allauth.socialaccount.providers.oauth2.views import (OAuth2Adapter, OAuth2LoginView, OAuth2CallbackView)
from .provider import IrcamAuthProvider
from django.conf import settings


class IrcamAuthAdapter(OAuth2Adapter):

    if not hasattr(settings, 'OAUTH_SERVER_BASEURL'):
        raise Exception("Couldn't find OAUTH_SERVER_BASEURL in the settings")
    if not hasattr(settings, 'OAUTH_SERVER_BASEURL_EXTERNAL'):
        raise Exception("Couldn't find OAUTH_SERVER_BASEURL_EXTERNAL in the settings")

    provider_id = IrcamAuthProvider.id
    access_token_url = '{}/o/token/'.format(settings.OAUTH_SERVER_BASEURL)  # Called programmatically, must be reachable from container
    authorize_url = '{}/o/authorize/'.format(settings.OAUTH_SERVER_BASEURL_EXTERNAL)  # Accessed by the client so must be host-reachable
    profile_url = '{}/profile/'.format(settings.OAUTH_SERVER_BASEURL)

    def complete_login(self, request, app, token, **kwargs):
        headers = {'Authorization': 'Bearer {0}'.format(token.token)}
        resp = requests.get(self.profile_url, headers=headers)
        extra_data = resp.json()
        return self.get_provider().sociallogin_from_response(request, extra_data)


oauth2_login = OAuth2LoginView.adapter_view(IrcamAuthAdapter)
oauth2_callback = OAuth2CallbackView.adapter_view(IrcamAuthAdapter)

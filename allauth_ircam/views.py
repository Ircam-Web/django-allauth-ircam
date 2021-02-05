import requests
from allauth.socialaccount.providers.oauth2.views import (OAuth2Adapter, OAuth2LoginView, OAuth2CallbackView)
from allauth.socialaccount.models import SocialApp
from .provider import IrcamAuthProvider
from .utils import create_or_update_local_entities
from django.conf import settings
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.utils.encoding import filepath_to_uri

class IrcamAuthAdapter(OAuth2Adapter):

    if not hasattr(settings, 'OAUTH_SERVER_BASEURL'):
        raise Exception("Couldn't find OAUTH_SERVER_BASEURL in the settings")

    provider_id = IrcamAuthProvider.id
    access_token_url = '{}/o/token/'.format(settings.OAUTH_SERVER_BASEURL)  # Called programmatically, must be reachable from container
    authorize_url = '{}/o/authorize/'.format(settings.USER_SERVER_BASEURL)  # Accessed by the client so must be host-reachable
    profile_url = '{}/profile/'.format(settings.OAUTH_SERVER_BASEURL)

    def complete_login(self, request, app, token, **kwargs):
        headers = {'Authorization': 'Bearer {0}'.format(token.token)}
        resp = requests.get(self.profile_url, headers=headers)
        extra_data = resp.json()
        print(extra_data)
        if getattr(settings, 'OAUTH2_IRCAM', False):
            create_or_update_local_entities(extra_data)
        return self.get_provider().sociallogin_from_response(request, extra_data)

def serverLogout(request):
    if not request.user.is_authenticated:
        pass
    else :
        logout(request)
        if not getattr(settings, 'OAUTH2_IRCAM', False):
            return redirect("/")
        else:
            if hasattr(settings, 'LOCAL_CLIENTAPP'):
                return redirect(settings.USER_SERVER_BASEURL+"/accounts/logout/?next=/logout_redirect/"+filepath_to_uri(settings.LOCAL_CLIENTAPP))
            else:
                app = SocialApp.objects.filter(provider='ircamauth')[0]
                return redirect(settings.USER_SERVER_BASEURL+"/accounts/logout/?next=/logout_redirect/"+filepath_to_uri(app.name))

oauth2_login = OAuth2LoginView.adapter_view(IrcamAuthAdapter)
oauth2_callback = OAuth2CallbackView.adapter_view(IrcamAuthAdapter)

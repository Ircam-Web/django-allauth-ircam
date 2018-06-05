from allauth.socialaccount import providers
from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider
from django.dispatch import receiver
from allauth.socialaccount.signals import social_account_updated


class IrcamAuthAccount(ProviderAccount):
    pass
    # def get_profile_url(self):
    #     return self.account.extra_data.get('profileUrl')

    # def get_avatar_url(self):
    #     return self.account.extra_data.get('avatar')

    # def to_str(self):
    #     dflt = super(IrcamAuthAccount, self).to_str()
    #     return self.account.extra_data.get('username', dflt)


class IrcamAuthProvider(OAuth2Provider):
    id = 'ircamauth'
    name = 'Ircam Auth'
    account_class = IrcamAuthAccount

    def extract_uid(self, data):
        return str(data['id'])

    def extract_common_fields(self, data):
        from pprint import pprint
        return dict(username=data['username'],
                    email=data['email'],
                    first_name=data['first_name'],
                    last_name=data['last_name'],)

    def get_default_scope(self):
        scope = ['read']
        return scope


@receiver(social_account_updated)
def handler(sender, **kwargs):
    from pprint import pprint
    local_user = kwargs['sociallogin'].user
    updated_data = kwargs['sociallogin'].account.extra_data
    # TODO: update local_user with updated_data received from the remote provider


providers.registry.register(IrcamAuthProvider)

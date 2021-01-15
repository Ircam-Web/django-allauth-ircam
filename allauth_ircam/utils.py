import logging
from allauth.account.models import EmailAddress
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings

logger = logging.getLogger('app')

def update_localuser(user, extra_data):
    if (
            user.email != extra_data['email'] or 
            user.first_name != extra_data['first_name'] or 
            user.last_name != extra_data['last_name'] 
        ):
        user.email = extra_data['email']
        user.first_name = extra_data['first_name']
        user.last_name = extra_data['last_name']
        user.save()
        logger.info('User {0} updated, email:{1}, firstN:{2}, LastN:{3}'
            .format(user.username, user.email, user.first_name, user.last_name))

def create_or_update_local_user(extra_data):
    users = User.objects.filter(username__iexact = extra_data['username'])
    if not users:
        user = User.objects.create(
            username = extra_data['username'],
            email = extra_data['email'],
            first_name = extra_data['first_name'],
            last_name = extra_data['last_name'],
            is_active = True
        )
        user.save()
        logger.info('Created user {0} (UID #{1})'.format(user.username, user.pk))

    else:
        if len(users) > 1:

            raise Exception("Multiple same username in DB...")
        else :
            user = users[0]
            update_localuser(user, extra_data) 
    return user

def create_or_update_local_entities(extra_data):
    ''' 
    Create or Update entities in relationship with datas contained in extra_data
    The entities are: User, SocialAccount, Email
    extra_data contains : username, email, first_name, last_name, avatar
    '''
    soc_accounts =  SocialAccount.objects.filter(uid = extra_data['id'], provider = 'ircamauth')
    if not soc_accounts:
        user = create_or_update_local_user(extra_data)
        # Creating the allauth social account so the user can log in through Ircam Auth
        soc_account = SocialAccount( user = user,
                                provider = 'ircamauth',
                                uid = extra_data['id'],
                                extra_data = extra_data )
        soc_account.save()
        logger.info('Created social account for user {0} (UID #{1})'.format( user.username, user.pk))
        email_addresses = EmailAddress.objects.filter(email = extra_data['email'])
        if not email_addresses:
            email_address = EmailAddress(email = extra_data['email'], user = user, primary = True, verified = False)  # Emails are created unverified by default, just doing the same. Anyway, if settings.ACCOUNT_EMAIL_VERIFICATION is "none" it doesn't matter.
            email_address.save()
            logger.info('Created email address for user {0} (UID #{1})'.format( user.username, user.pk))
        else:
            email_address = email_addresses[0]
            email_address.user = user
            email_address.save()

    else :
        user = User.objects.get(id = soc_accounts[0].user_id)
        update_localuser(user, extra_data)

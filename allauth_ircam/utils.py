import logging
from allauth.account.models import EmailAddress
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.contrib.auth.models import Group

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

def update_ircamintern_group(user,extra_data):
    '''
    If settings.ORGANIZATION_INTERN_USERS_GROUP is defined:
    1. automatic group creation if needed
    2. insertion/remove of the user, following is_internal_user boolean coming from auth server
    '''
    if 'is_internal_user' not in extra_data:
        return

    if getattr(settings, 'ORGANIZATION_INTERN_USERS_GROUP', False):
        group_name = settings.ORGANIZATION_INTERN_USERS_GROUP
        intern_users, created = Group.objects.get_or_create(name=group_name)
        is_user_intern = user.groups.filter(name = group_name).exists()
        if is_user_intern and extra_data['is_internal_user'] == False:
            user.groups.remove(intern_users)
            user.save()
        if is_user_intern == False and extra_data['is_internal_user'] == True :
            user.groups.add(intern_users)
    else:
        pass

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

    update_ircamintern_group(user,extra_data)
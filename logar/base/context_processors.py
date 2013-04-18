# -*- coding: utf8 -*-

from social_auth.models import UserSocialAuth


def user_avatar(request):
    if request.user.is_authenticated():
        try:
            screen_name = request.user.social_auth.get(provider='twitter').extra_data['screen_name']

            return {
                'user_avatar': "http://api.twitter.com/1/users/profile_image?screen_name={0}".format(
                    screen_name)
            }
        except (KeyError, UserSocialAuth.DoesNotExist):
            pass

    return {'user_avatar': None}


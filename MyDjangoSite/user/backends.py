# encoding=utf-8
from __future__ import unicode_literals
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class A():
    is_wrong_password = True


class MyBackends(ModelBackend):
    """
    Authenticates against settings.AUTH_USER_MODEL.
    """

    def authenticate(self, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
        try:
            user = UserModel._default_manager.get_by_natural_key(username)
            if user is None:
                user = UserModel._default_manager.get_by_email_key(username)
            if user is None:
                user = UserModel._default_manager.get_by_mobile_key(username)
            if user is None:
                raise UserModel.DoesNotExist(
                    "%s matching query does not exist." %
                    UserModel._meta.object_name
                )
            if user.check_password(password):
                return user
            else:
                user = A()
                return user
        except UserModel.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a non-existing user (#20760).
            UserModel().set_password(password)
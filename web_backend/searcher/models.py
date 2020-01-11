from __future__ import unicode_literals


from django.db import models
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _



class MyUser(AbstractBaseUser, PermissionsMixin):
    username = models.EmailField(_('email address'), unique=True)

    telegram_id = models.IntegerField(null=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []




# class MyUser(AbstractBaseUser, PermissionsMixin):
#     username = models.CharField(max_length=100, unique=True)
#     telegram_id = models.IntegerField(null=True)
#
#     objects = UserManager()
#
#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = []





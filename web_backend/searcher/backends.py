from django.contrib.auth.backends import BaseBackend

from searcher.models import MyUser
from django.contrib.sessions.models import Session


class SettingsBackend(BaseBackend):

    def authenticate(self, request, username=None, password=None):

        login_valid = bool(MyUser.objects.filter(username=username).count())
        pwd_valid = MyUser.objects.get(username=username).password == password

        if login_valid and pwd_valid:
            try:
                user = MyUser.objects.get(username=username)
            except MyUser.DoesNotExist:
                print("User dot exist")
                user = None

            return user
        return None

    def get_user(self, user_id):
        try:
            return MyUser.objects.get(pk=user_id)


        except MyUser.DoesNotExist:
            return None

    def has_perm(self, user_obj, perm, obj=None):
        return True

import logging

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

logger = logging.getLogger(__name__)


class AuthEmailModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        logger.info("User's using Email to login")
        if "@" not in username:
            return None
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None

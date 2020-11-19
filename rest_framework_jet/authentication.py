from django.contrib.auth.models import User
from django.utils.encoding import smart_str
from django.conf import settings

from rest_framework import authentication, exceptions

from jet.utils import hmac_sha256
from jet.exceptions import JETException


class JETAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = self.get_token(request)

        if not token:
            return None

        token = smart_str(token)

        try:
            decrypted_meta, decrypted_payload = settings.GLOBAL_JET.decrypt_from_PK(token)
        except JETException:
            raise exceptions.AuthenticationFailed('Bad token')

        try:
            user_id = decrypted_payload['id']
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No user found')

        return (user, decrypted_payload)

    def get_token(self, request):
        auth_header = authentication.get_authorization_header(request)

        if not auth_header:
            return None

        if len(auth_header.split()) != 2:
            return None

        prefix, token = auth_header.split()

        if smart_str(prefix) != 'JET':
            return None

        return token

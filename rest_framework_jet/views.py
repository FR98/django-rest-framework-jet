from django.shortcuts import render
from django.contrib.auth import authenticate
from django.conf import settings

from rest_framework import exceptions
from rest_framework.views import APIView
from rest_framework.response import Response

from jet.utils import hmac_sha256


class GenerateJET(APIView):

    def post(self, request, *args, **kwargs):
        username = request.data['username']
        password = request.data['password']

        user = authenticate(
            request,
            username = username,
            password = password
        )

        if not user:
            raise exceptions.AuthenticationFailed('Invalid credentials')

        if not user.is_active:
            raise exceptions.AuthenticationFailed('Not active')

        payload = {
            'id': user.id
        }

        user_secret = hmac_sha256(username, password, 'ascii')
        token = settings.GLOBAL_JET.encrypt(user_secret, payload)
        return Response({ "token": token })


class VerifyJET(APIView):

    def post(self, request, *args, **kwargs):
        token = request.data['token']

        if not token:
            raise exceptions.AuthenticationFailed('A token has not been generated')

        is_valid_token = settings.GLOBAL_JET.is_valid_token(token)
        return Response({ "valid": is_valid_token })



class RefreshJET(APIView):

    def post(self, request, *args, **kwargs):
        token = request.data['token']

        if not token:
            raise exceptions.AuthenticationFailed('A token has not been generated')

        new_token = settings.GLOBAL_JET.refresh_token(token)
        return Response({ "token": new_token })


generate_jet = GenerateJET.as_view()
verify_jet = VerifyJET.as_view()
refresh_jet = RefreshJET.as_view()

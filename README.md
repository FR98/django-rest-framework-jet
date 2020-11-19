=====
Rest Framework JET
=====

Rest Framework JET is a Django app to manage authentication. It can create tokens, verify and refresh them.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Install Django Rest Framework.

2. Add "rest_framework_jet" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'rest_framework_jet',
    ]

3. Configure JET

    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework_jet.authentication.JETAuthentication',
        )
    }

    GLOBAL_JET = JET(
        SECRET = SECRET_KEY
    )

4. Include the rest_framework_jet URLconf in your project urls.py like this::

    url(r'^api/token-auth/', generate_jet),
    url(r'^api/token-verify/', verify_jet),
    url(r'^api/token-refresh/', refresh_jet),

5. Start the development server

6. Visit http://127.0.0.1:8000/api/token-auth/
   to authenticate a user and generate a valid token.

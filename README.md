
<h2 align="center">Rest Framework JET</h2>
<h3 align="center">Rest Framework JET is a Django app to manage authentication. It can create tokens, verify and refresh them.</h3>

Detailed documentation is in the "docs" directory.

Quick start
-----------

*Install Django Rest Framework.

*Add "rest_framework_jet" to your INSTALLED_APPS setting like this:

    ```INSTALLED_APPS = [
        ...
        'rest_framework_jet',
    ]
    ```

*Configure JET

    ```REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework_jet.authentication.JETAuthentication',
        )
    }

    GLOBAL_JET = JET(
        SECRET = SECRET_KEY
    )
    ```

*Include the rest_framework_jet URLconf in your project urls.py like this:

    *url(r'^api/token-auth/', generate_jet),
    *url(r'^api/token-verify/', verify_jet),
    *url(r'^api/token-refresh/', refresh_jet),

*Start the development server

*Visit http://127.0.0.1:8000/api/token-auth/
   to authenticate a user and generate a valid token.

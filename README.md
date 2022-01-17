# google-oauth-token

use the [google-auth-oauthlib](https://github.com/googleapis/google-api-python-client/blob/main/docs/oauth.md) library to get a token for use with the [admin directory api](https://developers.google.com/admin-sdk/directory/v1/guides/authorizing).

specifically we're targeting the directory [users.update](https://developers.google.com/admin-sdk/directory/reference/rest/v1/users/update) API so we can modify some POSIX information for OS Login on GCP Compute Engine.

The important thing about this is the scopes we're requesting as part of the OAuth flow which are required for the API.

```
SCOPES = [
    "https://www.googleapis.com/auth/admin.directory.user",
    "https://www.googleapis.com/auth/admin.directory.user.readonly",
    "https://www.googleapis.com/auth/cloud-platform",
]
```


Steps (shamelessly ripped from [here](https://developers.google.com/identity/protocols/oauth2))
1. create a GCP project
2. under APIs & Services, click on Oauth consent screen and configure with your app name.  The users are *Internal*.
3. under APIs & services, click on Credentials and create Credentials for an OAuth Client ID. Set the Application Type to *Desktop app*.
4. A client ID and secret are generated.  download them to the directory where you cloned this repo and rename to `client_secrets.json`.


create a virtual env and pip install the requirements, then run `python login.py` to start the oauth flow.  A browser window should pop up. log in as a user who has admin access in Workspace/Cloud Identity.  The browser will redirect to a webserver the python app started and the console app should spit out an access token.

you can now use this access token to call Admin directory APIs.  you can try with the [users.get](https://developers.google.com/admin-sdk/directory/reference/rest/v1/users/get) API to make sure things work before you try the `users.update` method.

```
curl -H "Authorization: Bearer <token>` https://admin.googleapis.com/admin/directory/v1/users/<userKey>
```


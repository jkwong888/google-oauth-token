from google_auth_oauthlib.flow import InstalledAppFlow
from pprint import pprint

SCOPES = [
    "https://www.googleapis.com/auth/admin.directory.user",
    "https://www.googleapis.com/auth/admin.directory.user.readonly",
    "https://www.googleapis.com/auth/cloud-platform",
]

flow = InstalledAppFlow.from_client_secrets_file(
        'client_secrets.json',
        scopes=SCOPES)

flow.run_local_server(port=0)

credentials = flow.credentials
print(credentials.token)

import os
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from google.oauth2 import service_account
import googleapiclient.discovery

flags = tools.argparser.parse_args(args=[])


def get_credentials(scopes, client_secret_file, application_name):
    home_dir = os.path.expanduser('tmp')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'google-python-credentials.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(client_secret_file, scopes)
        flow.user_agent = application_name
        credentials = tools.run_flow(flow, store, flags)
        print('Storing credentials to ' + credential_path)
    return credentials


def get_service_credentials(service_account_file, scopes):
    credentials = service_account.Credentials.from_service_account_file(service_account_file, scopes=scopes)
    return credentials

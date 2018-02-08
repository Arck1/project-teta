from django.conf import settings

from googleapiclient.http import MediaIoBaseDownload
import httplib2
import io
from apiclient import discovery

import os
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

from google_api.auth import get_credentials

flags = tools.argparser.parse_args(args=[])
SCOPES = 'https://www.googleapis.com/auth/presentations'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Project_Teta'



def get_slides(id):
    credentials = get_credentials(SCOPES, CLIENT_SECRET_FILE, APPLICATION_NAME)
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('slides', 'v1', http=http)

    request = service.presentations().get(presentationId=id)
    response = request.execute()
    return response
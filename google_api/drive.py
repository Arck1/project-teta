from django.conf import settings

from googleapiclient.http import MediaIoBaseDownload
import httplib2
import io
from apiclient import discovery
from google_api.auth import get_credentials

SCOPES = 'https://www.googleapis.com/auth/drive'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Project_Teta'

def download_and_save_presentation_as_pdf(id):
    credentials = get_credentials(SCOPES, CLIENT_SECRET_FILE, APPLICATION_NAME)
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('drive', 'v3', http=http)

    request = service.files().export_media(fileId=id, mimeType='application/pdf')
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        # print("Download %d%%." % int(status.progress() * 100))
    f = open(settings.MEDIA_URL + id + '.pdf', 'wb')
    f.write(fh.getvalue())
    f.close()

    return settings.MEDIA_URL + id + '.pdf'


def files_export_media(id, mimeType):
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('drive', 'v3', http=http)
    request = service.files().export_media(fileId=id, mimeType=mimeType)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        # print("Download %d%%." % int(status.progress() * 100))
    return fh


def get_metadata(id):
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('drive', 'v3', http=http)
    request = service.files().get(fileId=id)
    response = request.execute()
    return response

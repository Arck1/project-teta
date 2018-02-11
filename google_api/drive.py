import googleapiclient
from django.conf import settings

from googleapiclient.http import MediaIoBaseDownload
import googleapiclient.discovery
import io
from google_api.auth import get_service_credentials


SCOPES = ['https://www.googleapis.com/auth/drive']

def download_and_save_presentation_as_pdf(id):
    credentials = get_service_credentials(settings.SERVICE_ACCOUNT_FILE, SCOPES)

    service = googleapiclient.discovery.build('drive', 'v3', credentials=credentials)

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
    credentials = get_service_credentials(settings.SERVICE_ACCOUNT_FILE, SCOPES)
    service = googleapiclient.discovery.build('drive', 'v3', credentials=credentials)
    request = service.files().export_media(fileId=id, mimeType=mimeType)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        # print("Download %d%%." % int(status.progress() * 100))
    return fh


def get_metadata(id):
    credentials = get_service_credentials(settings.SERVICE_ACCOUNT_FILE, SCOPES)
    service = googleapiclient.discovery.build('drive', 'v3', credentials=credentials)
    request = service.files().get(fileId=id)
    response = request.execute()
    return response

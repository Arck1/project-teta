from django.conf import settings

from apiclient import discovery
import googleapiclient.discovery

from google_api.auth import get_service_credentials

SCOPES = ['https://www.googleapis.com/auth/presentations']

def get_slides(id):
    credentials = get_service_credentials(settings.SERVICE_ACCOUNT_FILE, SCOPES)
    service = googleapiclient.discovery.build('slides', 'v1', credentials=credentials)

    request = service.presentations().get(presentationId=id)
    response = request.execute()
    return response

def get_thumbnail(presentationId, pageObjectId):
    credentials = get_service_credentials(settings.SERVICE_ACCOUNT_FILE, SCOPES)
    service = discovery.build('slides', 'v1', credentials=credentials)

    request = service.presentations().getThumbnail(presentationId=presentationId, pageObjectId=pageObjectId)
    response = request.execute()

    return response

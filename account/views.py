from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import auth
from account.forms import SlidesForm
from account.models import Presentation
import google.auth
import googleapiclient
import google.oauth2.credentials
from google.oauth2 import service_account



# Create your views here.

@login_required
def account_info(request):
    presentations = Presentation.objects.filter(user=auth.get_user(request))
    return render(request, 'account.html', locals())

@login_required
def presentation_info(request, id=0):
    print(id)
    id = int(id)
    if id <= 0:
        return redirect('/account/presentations/')
    presentation = Presentation.objects.get(id=id)
    if presentation is None:
        return redirect('/account/presentations/')
    return render(request, 'presentation.html', locals())


@login_required
def add_presentation(request):
    form = SlidesForm(request.GET)
    if request.POST:
        print(111)
        newslidesform = SlidesForm(request.POST)
        presentation = Presentation(request.POST)
        presentation.name = newslidesform["name"]
        presentation.description = newslidesform["description"]
        presentation.url = newslidesform["url"]
        presentation.user = auth.get_user(request)
        print(presentation)
        file_url = presentation.url.value()
        start = file_url.find("/d/") + 3
        end = file_url.find("/edit")
        presentation.presentationId = file_url[start:end]
        download_presentation_as_pdf(presentation.presentationId)
        # presentation.save()
        return redirect('/account/')

    return render(request, 'upload_presentation.html', locals())


def download_presentation_as_pdf(id):
    #credentials = service_account.Credentials.from_service_account_info()

    print(credentials)
    print(id)

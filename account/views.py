import argparse

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import auth

from account.forms import SlidesForm
from account.models import Presentation
from google_api.drive import download_and_save_presentation_as_pdf
from google_api.slides import get_slides
#

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
        newslidesform = SlidesForm(request.POST)
        presentation = Presentation(request.POST)
        presentation.name = newslidesform["name"]
        presentation.description = newslidesform["description"]
        presentation.url = newslidesform["url"]
        presentation.user = auth.get_user(request)
        file_url = presentation.url.value()
        start = file_url.find("/d/") + 3
        end = file_url.find("/edit")
        presentation.presentationId = file_url[start:end]
        # res = get_slides(presentation.presentationId)
        # print(res)
        #pdf_path = download_and_save_presentation_as_pdf(presentation.presentationId)
        #presentation.pdf = pdf_path
        #presentation.save()
        Presentation.objects.create(name=presentation.name,)
        return redirect('/account/')

    return render(request, 'upload_presentation.html', locals())



import re

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import auth

from account.forms import SlidesForm
from account.models import Presentation
from google_api.drive import download_and_save_presentation_as_pdf
from google_api.slides import get_slides
from google_api.drive import files_export_media
from project_teta import settings
import hashlib
from django.core.files import File

#

# Create your views here.

@login_required
def account_info(request):
    presentations = Presentation.objects.filter(user=auth.get_user(request))
    return render(request, 'account.html', locals())


@login_required
def presentation_info(request, id=0):
    id = int(id)
    link = ""
    if id <= 0:
        return redirect('/account/presentations/')
    presentation = Presentation.objects.get(id=id)
    status = ""
    if presentation.is_active:
        status = "Close"
    else:
        status = "Open"

    if presentation is None:
        return redirect('/account/presentations/')
    if request.POST.get('link'):
        if presentation.is_active:
            link = "http://127.0.0.1:8000/show/%d/%s/" % (presentation.id, presentation.hash)
            return render(request, 'presentation.html', locals())
        else:
            link = "presentation is closed"
            print(link)
            return render(request, 'presentation.html', locals())
    if request.POST.get('status'):
        presentation.is_active = not presentation.is_active
        presentation.save()
        if presentation.is_active:
            status = "Close"
        else:
            status = "Open"
    link = ""
    return render(request, 'presentation.html', locals())


@login_required
def add_presentation(request):
    form = SlidesForm(request.GET)
    if request.POST:
        newslidesform = SlidesForm(request.POST, request.FILES)
        if newslidesform.is_valid():
            presentation = Presentation()
            presentation.name = newslidesform["name"].value()
            presentation.description = newslidesform["description"].value()
            presentation.url = newslidesform["url"].value()
            presentation.user = auth.get_user(request)
            file_url = presentation.url
            start = file_url.find("/d/") + 3
            end = file_url.find("/edit")
            presentation.presentationId = file_url[start:end]
            pdf_s = newslidesform['pdf'].value()
            f = None
            if pdf_s is None:
                fh = files_export_media(presentation.presentationId, 'application/pdf')
                f = open(settings.MEDIA_URL + "user_files/" + presentation.presentationId + ".pdf", 'wb')
                f.write(fh.getvalue())
                f.close()
                f = open(settings.MEDIA_URL + "user_files/" + presentation.presentationId + ".pdf", 'rb')
                pdf_s = File(f)

            # Assumes the default UTF-8
            hash = hashlib.md5(presentation.name.encode()).hexdigest()
            presentation.hash = hash
            presentation.pdf.save(presentation.presentationId + ".pdf", pdf_s)
            # Presentation.objects.create(name=presentation.name, description=presentation.description,
            #                             url=presentation.url,
            #                             presentationId=presentation.presentationId, pdf=pdf_s, user=presentation.user,
            #                             hash=hash)
            if f is not None:
                f.close()
            return redirect('/account/')
        else:
            form = SlidesForm(request.POST)

    return render(request, 'upload_presentation.html', locals())

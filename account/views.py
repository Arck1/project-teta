import re

import time
from distutils.command import register

from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.contrib import auth

from account.forms import SlidesForm
from account.models import Presentation, PresentationCopy
from google_api.drive import files_export_media
from project_teta import settings
import hashlib
from django.core.files import File
from django.template.defaulttags import register
import urllib
import json


@register.filter
def get_item0(dictionary, key):
    val = dictionary.get(key)
    if val:
        return int(val[0])
    return 0
@register.filter
def get_item1(dictionary, key):
    val = dictionary.get(key)
    if val:
        return int(val[1])
    return 0
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

    if request.POST.get('status'):
        presentation.is_active = not presentation.is_active
        presentation.save()
        if presentation.is_active:
            status = "Close"
        else:
            status = "Open"
    link = ""

    if request.POST.get('add_link'):
        pcopy = PresentationCopy()
        pcopy.origin = presentation
        pcopy.name = request.POST['name']
        magic = pcopy.name + str(time.time())
        pcopy.hash = hashlib.md5(magic.encode()).hexdigest()
        pcopy.save()

    if request.POST.get('delete'):
        idc = request.POST['copy_id']
        obj = PresentationCopy.objects.get(id=idc)
        PresentationCopy.delete(obj)

    api_url = 'https://api-metrika.yandex.ru/stat/v1/data?'
    counter_id = "id=47725444"
    metrics = '&metrics=ym:pv:pageviews,ym:pv:users'
    dimensions = '&dimensions=ym:pv:URLPath'
    auth_token = '&oauth_token=AQAAAAAOGSvpAATQtPCjgBAfGU1wobj5hSPXApg'
    filter_url = '&filters=ym:pv:URLPath=~%27/show/' + str(presentation.id) + '/[0-9]%2B/*%27'
    request_url = api_url + counter_id + metrics + dimensions + filter_url + auth_token
    print(request_url)
    f = urllib.request.urlopen(request_url)
    ans = f.read()
    json_ans = json.loads(ans)
    data = json_ans['data']

    view_stat = {}

    for item in data:
        path = item['dimensions'][0]['name'].strip().split('/')
        view_stat[int(path[3])] = item['metrics']

    print(view_stat)

    copys = PresentationCopy.objects.filter(origin=presentation)
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



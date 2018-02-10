from django.shortcuts import render, redirect
import hashlib


# Create your views here.
from account.models import Presentation


def showcase(request, id=0, hash='none'):
    id = int(id)
    if id <= 0:
        return redirect('/')
    presentation = Presentation.objects.get(id=id)
    if presentation is None or presentation.hash != hash or not presentation.is_active:
        return redirect('/')

    return render(request, 'showcase.html', locals())

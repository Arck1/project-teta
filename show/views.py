from django.shortcuts import render, redirect
import hashlib

# Create your views here.
from account.models import Presentation, PresentationCopy


def showcase(request, id=0, copy_id=0, hash='none'):
    id = int(id)
    copy_id = int(copy_id)
    if id <= 0 or copy_id <= 0:
        return redirect('/')
    presentation = Presentation.objects.get(id=id)
    presentation_copy = PresentationCopy.objects.get(id=copy_id)

    if presentation_copy is None or presentation_copy.origin.id != id or presentation_copy.hash != hash \
            or not presentation.is_active:
        return redirect('/')

    return render(request, 'showcase.html', locals())

from django.db import models
from django.contrib.auth.models import User

class Presentation(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True, default='Another useless presentation')
    url = models.URLField(blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    presentationId = models.CharField(max_length=64, blank=True, null=True, default=None)
    user = models.ForeignKey(User, blank=True, null=True, default=None, on_delete=models.CASCADE)
    pdf = models.FilePathField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

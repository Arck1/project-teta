from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth.models import User
from project_teta import settings


class Presentation(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True, default='Another useless presentation')
    url = models.URLField(blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    presentationId = models.CharField(max_length=64, blank=True, null=True, default=None)
    user = models.ForeignKey(User, blank=True, null=True, default=None, on_delete=models.CASCADE)
    pdf = models.FileField(blank=True, null=True, default=None, upload_to='user_files/',
                           validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)
    hash = models.CharField(max_length=64, blank=True, null=True, default='xyz')

    stat = models.TextField(blank=True, null=True, default='[]')
    def __str__(self):
        try:
            return self.name
        except:
            return self.id

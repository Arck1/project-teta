from django.contrib import admin
from account.models import Presentation
# Register your models here.

class PresentationAdmin(admin.ModelAdmin):
    list_display = [ 'name', 'id', 'presentationId', 'user', 'is_active', 'pdf']

    class Meta:
        model = Presentation

admin.site.register(Presentation, PresentationAdmin)
from django.contrib import admin
from account.models import Presentation, PresentationCopy
# Register your models here.

class PresentationCopyInline(admin.StackedInline):
    model = PresentationCopy
    extra = 0

class PresentationAdmin(admin.ModelAdmin):
    list_display = [ 'name', 'id', 'presentationId', 'user', 'is_active', 'pdf']
    inlines = [PresentationCopyInline]

    class Meta:
        model = Presentation


admin.site.register(Presentation, PresentationAdmin)

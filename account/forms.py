from django import forms
from account.models import Presentation

class SlidesForm(forms.ModelForm):
    class Meta:
        model = Presentation
        fields = ["name", "url", "description"]

class PresentationEditForm(forms.ModelForm):
    class Meta:
        model = Presentation
        fields = ["name", "url", "description"]
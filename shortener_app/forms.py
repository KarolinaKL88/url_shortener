from django import forms
from shortener_app.models import AliasedUrl


class AliasedUrlForm(forms.Form):
    url = forms.URLField()

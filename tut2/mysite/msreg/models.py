from __future__ import unicode_literals

from django.db import models
from django import forms
# Create your models here.

class UploadFileForm(forms.Form):
    mstitle = forms.CharField(max_length=50)
    msfile = forms.FileField()

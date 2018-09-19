from django import forms

from django.utils.translation import ugettext_lazy as _
#from django.core import validators

from TypeIn.models import Diagnosis


class DiagnosisForm (forms.ModelForm):


    class Meta:
        model = Diagnosis
        fields = ['diagnosis_documented', 'status']
        labels = {
            "diagnosis_documented": _("Probably you mean"),
        }
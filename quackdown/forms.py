from django import forms
from django.forms import ModelForm
from stopspam.forms.fields import HoneypotField
from models import ClaimToInvestigate

class ClaimToInvestigateForm(ModelForm):
    error_css_class = 'error'
    required_css_class = 'required'
    
    accept_terms = HoneypotField()
        
    class Meta(object):
        model = ClaimToInvestigate
        widgets = {
               'claim_date': forms.TextInput(attrs={'class': 'datepicker'}),
        }
        
    
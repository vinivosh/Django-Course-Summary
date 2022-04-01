from dataclasses import fields
from django import forms



class ParticipantForm(forms.Form):
    email = forms.EmailField(label='Your email')
from django import forms

from .models import Rechnung

class RechnungForm(forms.ModelForm):

    class Meta:
        model = Rechnung
        fields = ('user_id', 'leistung', 'betrag', )
        labels = {
            "user_id": "Kunde"
        }
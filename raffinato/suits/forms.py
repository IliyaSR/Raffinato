from django import forms
from raffinato.suits.models import Suit


class BaseForm(forms.ModelForm):
    class Meta:
        model = Suit
        fields = ['name', 'personal_photo', 'price']


class AddForm(BaseForm):
    pass

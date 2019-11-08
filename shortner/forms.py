from .models import urldetails
from django import forms


class urldetailsForm(forms.ModelForm):
    class Meta:
        model = urldetails
        exclude = ('user', 'status', 'short_url', 'key', 'app_status')
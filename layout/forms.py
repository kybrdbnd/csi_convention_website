from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField(required=True)
    phone = forms.DecimalField(required=False)
    email = forms.EmailField(required=True)
    message = forms.CharField(required=True)

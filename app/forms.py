from django import forms


class MailForm(forms.Form):
    sender_name = forms.CharField(required=True)
    sender_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(required=True)

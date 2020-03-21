from django import forms


class MailForm(forms.Form):
    sender_name = forms.CharField()  # max_length=50, blank=False)
    sender_email = forms.EmailField()  # blank=False)
    subject = forms.CharField()  # max_length=100, blank=False)
    message = forms.CharField()

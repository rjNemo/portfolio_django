from portfolio.settings import EMAIL_HOST_USER,  DEFAULT_FROM_EMAIL
import requests
from datetime import datetime

""" Mailer Service used to send messages using API WebHooks.
    All Mailers must implement the following methods:

    def send_confirmation(name, email)->void

    def send_notification(name, email, subject, message)->void

    def send_quotation(name, email)->void
        """

URL = "https://hooks.zapier.com/hooks/catch/4071838/o98akab/"


def send_confirmation(name, email):
    """ Send confirmation message to customer """

    payload = {
        "mail_to": email,
        "from_name": DEFAULT_FROM_EMAIL,
        "reply_to": EMAIL_HOST_USER,
        "subject": f"👋Hello {name}, I received your message",
        "body": f"Dear {name}, \nYour message has been successfully sent. I will answer shortly.\nThank you for your patience,\nBest regards\n\nRuidy Nemausat\n (This is an automated message.)"
    }

    resp = requests.post(URL, data=payload)


def send_notification(name, email, subject, message):
    """ Send notification to admins """

    payload = {
        "mail_to": EMAIL_HOST_USER,
        "from_name": DEFAULT_FROM_EMAIL,
        "reply_to": EMAIL_HOST_USER,
        "subject": f"{name} a envoyé un message",
        "body": f"Sujet : {subject}\nDe : {name}, {email}\nLe : {datetime.now()}\nMessage : {message}\n"
    }

    resp = requests.post(URL, data=payload)

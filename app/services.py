from django.core.mail import mail_admins, send_mail
from portfolio.settings import EMAIL_HOST_USER


def send_mails(params):
    # send confirmation mail to sender
    CONFIRMATION_SUBJECT = f"Message recieved"
    CONFIRMATION_TEXT = f"Hello {params.sender_name},\nI have recieved your message and I will bet back to you shortly.\nBest regards,\nRuidy Nemausat"

    send_mail(
        CONFIRMATION_SUBJECT,
        CONFIRMATION_TEXT,
        from_email=EMAIL_HOST_USER,
        recipient_list=[params.sender_email]
    )

    # send message to ADMINS
    ADMIN_SUBJECT = "New message from Portfolio"
    ADMIN_TEXT = f"{params.sender_name} sent you a message\nSubject: {params.subject}\nMessage: {params.message}"
    mail_admins(
        ADMIN_SUBJECT,
        mail_params.message
    )

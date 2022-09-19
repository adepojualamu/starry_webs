from luke_portfolio.settings import EMAIL_HOST_USER
from django.core.mail import EmailMessage
import pathlib


def send_email(receiver, subject, content):
    try:

        msg = EmailMessage(
            subject,
            content,
            EMAIL_HOST_USER,
            [receiver]
        )
        msg.content_subtype = "html"
        msg.send()

    except:
        print(f"Couldn't send the email")
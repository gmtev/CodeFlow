from django.template.loader import render_to_string
from mailjet_rest import Client
from django.conf import settings


def send_welcome_email(email, username):
    mailjet = Client(auth=(settings.MAILJET_API_KEY, settings.MAILJET_SECRET_KEY), version='v3.1')
    html_content = render_to_string('accounts/email-greeting.html', {'username': username})
    data = {
        'Messages': [
        {
            'From': {
                'Email': 'codeflowforapp@gmail.com',
                'Name': 'CodeFlow',

            },
            'To': [
                {
                'Email': email,
                'Name': username,
                }
            ],
            'Subject': 'Welcome to CodeFlow',
            'TextPart': 'Welcome to CodeFlow!',
            'HTMLPart': html_content,
            }
        ]
    }
    result = mailjet.send.create(data=data)

def send_goodbye_email(email, username):
    mailjet = Client(auth=(settings.MAILJET_API_KEY, settings.MAILJET_SECRET_KEY), version='v3.1')
    html_content = render_to_string('accounts/email-goodbye.html', {'username': username})
    data = {
        'Messages': [
        {
            'From': {
                'Email': 'codeflowforapp@gmail.com',
                'Name': 'CodeFlow',

            },
            'To': [
                {
                'Email': email,
                'Name': username,
                }
            ],
            'Subject': 'We will miss you!',
            'TextPart': 'Welcome to CodeFlow!',
            'HTMLPart': html_content,
            }
        ]
    }
    result = mailjet.send.create(data=data)
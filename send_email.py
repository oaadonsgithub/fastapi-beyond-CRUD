import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='oaausc@gmail.com',
    to_emails='oaaderibigbe@usfca.edu',
    subject='Hello from SendGrid',
    html_content='<strong>Hello, Email!</strong>')
try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(f"Status Code: {response.status_code}")
    print(f"Body: {response.body}")
    print(f"Headers: {response.headers}")
except Exception as e:
    print(f"Error: {e}")

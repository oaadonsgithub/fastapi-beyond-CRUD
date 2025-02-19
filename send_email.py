import os
from datetime import datetime

import sendgrid
from dotenv import load_dotenv

load_dotenv()

sg = sendgrid.SendGridAPIClient(os.environ.get("SENDGRID_API_KEY"))

def send_email():
    today = datetime.today()
    week_number, year = today.isocalendar()[1], today.year
   ]
    positions_section = "".join(positions_html)
    country = country.title()
    message = sendgrid.Mail(
        from_email=(os.environ.get("FROM_EMAIL"), "Email Notification"),
        to_emails=(os.environ.get("TO_EMAILS"), ""),
        subject=f"",
        html_content=f"""
  
         """,
    )
    try:
        sg.send(message)
    except Exception as e:
        print(f"Error sending email: {e}.")
    else:
        print("Email sent successfully")

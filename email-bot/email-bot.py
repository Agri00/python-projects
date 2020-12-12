import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Your name'
email['to'] = 'example@gmail.com'
email['subject'] = 'Test'

email.set_content(html.substitute(name= 'dummy'))

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('youremail@gmail.com', 'yourpassword')
    smtp.send_message(email)
    print('all good boss!')

import smtplib
import email.utils
from email.mime.text import MIMEText

# Create the message
msg = MIMEText('This is the body of the message.')

msg['Subject'] = 'Simple test message'

server = smtplib.SMTP_SSL('smtp.gmail.com:465')
server.login('antoni.bonacic@icloud.com', '')
server.sendmail('antoni.bonacic@icloud.com', 'anteprojic@gmail.com', msg.as_string())
server.quit()
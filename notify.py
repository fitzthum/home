import settings
import secret

import smtplib
from email.header import Header
from email.mime.text import MIMEText


def email(subject,body):
  # connect
  server = smtplib.SMTP('smtp.gmail.com:587')
  server.ehlo()
  server.starttls()
  # log in
  server.login(secret.email_account,secret.email_password)
  
  msg = MIMEText(body,'plain','utf-8')
  msg['From'] = Header("{}@gmail.com".format(secret.email_account),"utf-8")
  msg['To'] = Header(settings.contact_address,"utf-8")
  msg['Subject'] = Header(subject,"utf-8")

  server.sendmail("{}@gmail.com".format(secret.email_account),settings.contact_address,msg.as_string())
  server.quit()

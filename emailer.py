#!/usr/bin/python3

import smtplib
import pers_data

print(pers_data.login, pers_data.password, pers_data.domain)
# print(dir(smtplib))

sender=pers_data.login+'@'+pers_data.domain
receivers=['q121212@gmail.com']
message = """From: Sender <kot@ya.ru>
To: Max R. <q121212@gmail.com>
MIME-Version: 1.0
Content-type: text/html
Subject: SMTP HTML e-mail test

This is an e-mail message to be sent in HTML format

<b>This is HTML message.</b>
<h1>This is headline.</h1>
"""

try:
   # smtpObj = smtplib.SMTP_SSl()
   smtpObj = smtplib.SMTP('smtp.'+pers_data.domain)
   smtpObj.set_debuglevel(1)
   smtpObj.starttls()
   smtpObj.ehlo()
   smtpObj.login(pers_data.login, pers_data.password)	
   smtpObj.sendmail(sender, receivers, message)         
   print("Successfully sent email")
except smtplib.SMTPException as e:
   print("Error: unable to send email:", e)
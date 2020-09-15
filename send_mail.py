
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


port = 465

mail_id = "alexhunterfake123@gmail.com"
password = "helloworld567"

# Creating a secure SSL context
context = ssl.create_default_context()


def send_mail(subject="hello there", body="This is a message", from_email="Durgesh <alexhunterfake123@gmail.com>", to_mails=[]):
    assert isinstance(to_mails, list)
    # print(from_email)
    # print(to_mails)

    # message_str = "hey there this is a test message"

    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = ", ".join(to_mails)
    msg["Subject"] = subject
    txt_part = MIMEText(body, 'plain')
    msg.attach(txt_part)

    html_part = MIMEText("""
    <html>
        <head></head>
        <body>
            <b>This is bold</b>
            <br>
            <i>This is italic</i>
        </body>
    </html>
    """, 'html')
    msg.attach(html_part)

    message_str = msg.as_string()

    # loggin in to server
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls(context=context)
    server.login(mail_id, password)
    server.sendmail(from_addr=from_email, to_addrs=to_mails, msg=message_str)
    server.quit()


send_mail(to_mails=['therajtiwari254@gmail.com'])

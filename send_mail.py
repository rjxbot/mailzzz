
import smtplib
import ssl


port = 465


mail_id = "alexhunterfake123@gmail.com"
password = "helloworld567"

# Creating a secure SSL context
context = ssl.create_default_context()


def send_mail(subject="hello there", body="This is a message", from_email=mail_id, to_mails=[]):
    assert isinstance(to_mails, list)

    message_str = "hey there this is a test message"
    # loggin in to server
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls(context=context)
    server.login(from_email, password)
    server.sendmail(from_addr=mail_id, to_addrs=to_mails, msg=message_str)
    server.quit()


send_mail(to_mails=['therajtiwari254@mgmail.com', 'nidhitiwari2574@gmail.com'])

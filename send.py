import sys
from send_mail import send_mail


def message(name, event, date):
    msg = "Hello {}\nYou are invited to join {} dated on {}.\nSee you there.".format(
        name, event, date)
    return msg


to = ['therajtiwari254@gmail.com']

if __name__ == "__main__":
    print(sys.argv)
    lis = sys.argv
    if (len(lis) > 3):
        msg = message(lis[1], " ".join(lis[2:-1]), lis[-1])
        send_mail(body=msg, to_mails=to)
    else:
        print("Invalid input")


# python3 send.py Raj Python Workshop 19/09/2020

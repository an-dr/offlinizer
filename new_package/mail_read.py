from imap_tools import MailBox
import os

EMAIL = os.environ.get('OFF_MAIL')
PASSWORD = os.environ.get('OFF_PASSWORD')
MAIL_SERVER = os.environ.get('OFF_SERVER')
MAIL_PORT = 993

with MailBox(MAIL_SERVER).login(EMAIL, PASSWORD) as mailbox:
    subjects = [msg.subject for msg in mailbox.fetch()]
    cont = [msg.text for msg in mailbox.fetch()]

print(subjects)
print(cont)
# OR the same otherwise
# with MailBox('imap.mail.com').login('test@mail.com', 'password') as mailbox:
#     subjects = [msg.subject for msg in mailbox.fetch()]
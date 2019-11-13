from functools import partial
import email
import imaplib #imap pop
import sys

#auto fill, no param needed
def connect(self, name="user", email='rideruniversitytest2019@gmail.com', pwd='Rider2019'):
    ''' connects to the gmail server'''

    username = email
    password = pwd
    converted_emails = []

    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(username, password)

    # select inbox folder ( folders can be list w/ mail.list()
    mail.select("inbox")

    # create a new folder
    mail.create("fakeEmails")

    # search inbox for all mail, ALL keyword for all results
    result, data = mail.uid('search', None, "ALL")

    ids = data[0]  # data is a list.
    id_list = ids.split()  # ids is a space separated string

    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    def get_first_text_block( email_message_instance):
        ''' email contains multiple payloads (plaintext/ html), this method parse each message separately'''
        maintype = email_message_instance.get_content_maintype()
        if maintype == 'multipart':
            for part in email_message_instance.get_payload():
                if part.get_content_maintype() == 'text':
                    return part.get_payload()
        elif maintype == 'text':
            return email_message_instance.get_payload()

    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


    # go throught every item in id_list
    for item in id_list:
        # latest_email_uid = data[0].split()[-1] # get the latest = newest email

        result2, data = mail.uid('fetch', item, '(RFC822)')  # fetch the email body (RFC822) for the given ID

        raw_email = data[0][1]  # here's the body, which is raw text of the whole email
        # including headers and alternate payloads

        # decode data
        raw_email = data[0][1].decode("utf-8")

        # user email library to create email object
        import email
        email_message = email.message_from_string(raw_email)

        # get message header
        to_ = email_message['To']
        from_ = email_message['From']
        subject_ = email_message['Subject']
        date_ = email_message['date']

        email = get_first_text_block(email_message)

        # store email in a list
        ready_email = (email, to_, from_, subject_, date_)

        converted_emails.append(ready_email)

    senders_list = []
    subject_list = []
    date_list = []
    email_dic = {}
    email_body = []

    for item in converted_emails:
        subject_list.append(item[3])

    for email in converted_emails:
        senders_list.append(email[2])

    for item in converted_emails:
        date_list.append(item[4])

    for item in converted_emails:
        email_body.append(item[0])

    i = 1
    for email in converted_emails:
        email_dic['MSG'+str(i)] = email[0]
        i += 1

    return senders_list , subject_list, email_dic, date_list, converted_emails





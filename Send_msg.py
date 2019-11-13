import smtplib, ssl


def send(username = "rideruniversitytest2019@gmail.com",password ="Rider2019",reciver = "jelenb@rider.edu",
                                                subject = "what is for dinner", body = "this is my message"):

    '''Sends a message using SMTP protocol // 587'''

    print("im working on that message...")
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls

    # connect to the smtp server
    with smtplib.SMTP(smtp_server, port) as smtp:
        smtp.ehlo() # open connection
        smtp.starttls() # encrypt connection
        
        smtp.ehlo()

        smtp.login(username, password) # send pwd n username

        subject = subject
        body = body
        msg = f'Subject: {subject}\n\n{body}'

        #send message (from , to, msg)
        smtp.sendmail(username,reciver, msg)

        smtp.quit()
        print("success, msg sent to : " + reciver)

# test
if __name__ == "__main__":
    send()

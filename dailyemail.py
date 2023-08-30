#!/usr/bin/python

import smtplib
from dbConnect import dbConnect
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email configuration
sender_email = "chu.kevin.h@gmail.com"
sender_name = "Kevin Chu"
sender_password = "crzkkvpicoqwyoxa"
subject = "Weekly Update"


# Connect to Database
empDB = dbConnect()
empRecords = empDB.getEmployeeRecords()

for emp in empRecords:
    # Load user email
    recipient_name = emp[0] + " " + emp[1]
    recipient_email = emp[2]
    # Create the MIME object
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["Subject"] = subject
    msg["To"] = recipient_email

    # HTML content
    with open(r"C:\Users\Kevin\Desktop\Personal-Projects\weeklyEmail\emailtemp.html") as file:
            email_template = file.read()
    modified_email_template = email_template.replace("[Recipient's Name]", recipient_name)
    modified_email_template = modified_email_template.replace("[Your Name]", sender_name)
    msg.attach(MIMEText(modified_email_template, "html"))

    try:
        # Connect to the SMTP server
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(sender_email, sender_password)
        # Send the email
        server.sendmail(sender_email, recipient_email, msg.as_string())
        print("Successfully sent email")
        server.quit()
    except smtplib.SMTPException as e:
        print("Error: unable to send email")
        print(e)

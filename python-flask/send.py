import smtplib

sender = "DevOps Trainer <devopstrainerfawb@gmail.com>"
receiver = "Sruniraj PC <srunirajpc@gmail.com>"

message = f"""\
Subject: Sample Mail
To: {receiver}
From: {sender}

This is a test e-mail message."""

with smtplib.SMTP("smtp.mailtrap.io", 387) as server:
    server.login("devopstrainerfawb@gmail.com", "Fico@12345")
    server.sendmail(sender, receiver, message)

class MailSender:
    def __init__(self, titlu, continut):
        import smtplib, ssl
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart


        server_mail = 'smtp.gmail.com' # this is configured for gmail
        port = 465
        sender = 'generic@gmail.com' # change to the email (gmail) you have configured to receive emails from
        password = 'fakePassword1234' # input your password
        receiver = '' # inseert email of the receiver (your email address where you want to receive notifications)
        message = MIMEMultipart()
        message['Subject'] = titlu
        message['From'] = sender
        message['To'] = receiver
        mail_ca_text = continut

        part1=MIMEText(mail_ca_text, 'plain')
        message.attach(part1)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(server_mail, port, context = context) as server:
            server.login(sender, password)
            server.sendmail(sender, receiver, message.as_string())
            

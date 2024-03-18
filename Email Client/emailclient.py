import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, recipient_email, subject, message):
    try:
        # Set up the SMTP server
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.login(sender_email, sender_password)

        # Create a MIMEText object to represent the email
        email_message = MIMEMultipart()
        email_message['From'] = sender_email
        email_message['To'] = recipient_email
        email_message['Subject'] = subject

        # Attach the message to the email
        email_message.attach(MIMEText(message, 'plain'))

        # Send the email
        smtp_server.send_message(email_message)

        print("Email sent successfully!")

    except Exception as e:
        print("An error occurred:", str(e))
    finally:
        smtp_server.quit()

# Example usage
sender_email = "your_email@gmail.com"
sender_password = "your_password"
recipient_email = "recipient_email@example.com"
subject = "Test Email"
message = "This is a test email sent from Python."

send_email(sender_email, sender_password, recipient_email, subject, message)

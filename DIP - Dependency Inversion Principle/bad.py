# Bad example violating DIP

class EmailSender:
  def send_email(self, to, message):
    print(f"Sending email to {to}: {message}")
    # Code to send email


class NotificationService:
  def __init__(self):
    self.email_sender = EmailSender()

  def send_notification(self, to, message):
    self.email_sender.send_email(to, message)

# Good example following DIP

class EmailSender:
  def send_email(self, to, message):
    print(f"Sending email to {to}: {message}")
    # Code to send email


class NotificationSender:
  def send_notification(self, to, message):
    raise NotImplementedError("send_notification() method must be implemented in concrete classes")


class EmailNotificationSender(NotificationSender):
  def __init__(self, email_sender):
    self.email_sender = email_sender

  def send_notification(self, to, message):
    self.email_sender.send_email(to, message)


class NotificationService:
  def __init__(self, notification_sender):
    self.notification_sender = notification_sender

  def send_notification(self, to, message):
    self.notification_sender.send_notification(to, message)

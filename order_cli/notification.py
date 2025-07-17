class NotificationSender:
    def send(self, message):
        raise NotImplementedError()

class EmailSender(NotificationSender):
    def send(self, message):
        print(f"[EMAIL] {message}")

class SMSSender(NotificationSender):
    def send(self, message):
        print(f"[SMS] {message}")

# Abstraction
"""we abstrct all the detail of sending an email in send_email method"""


class EmailService:

    def _connect(self):
        print("Connecting to email server")

    def _authenticate(self):
        print("Authenticating...")

    def send_Email(self):
        self._connect()
        self._authenticate()
        print("Sending email....")
        self._disconnect()

    def _disconnect(self):
        print("Disconnecting from an Email server...")

email = EmailService()
email.send_Email()

"""the send_email method abstracts away the unwated stps for the user to carry on,
which focus more on simplfying usage by hiding uncessary details.
"""

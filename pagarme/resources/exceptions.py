class GatewayException(Exception):
    def __init__(self, message="Gateway exception"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message
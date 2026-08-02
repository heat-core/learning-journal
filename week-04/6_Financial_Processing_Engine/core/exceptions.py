class InsufficientFundsError(Exception):
    def __init__(self, message="Insufficient funds for this transaction."):
        self.message = message
        super().__init__(self.message)


class InvalidAmountError(Exception):
    def __init__(self, message="Amount must be greater than zero."):
        self.message = message
        super().__init__(self.message)
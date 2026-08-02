from core.exceptions import InsufficientFundsError, InvalidAmountError
from utils.decorators import log_transaction

class BankAccount():
    def __init__(self, account_number: str, owner: str, initial_balance: float = 0.0):
        self.account_number = account_number
        self.owner = owner

        if initial_balance < 0 :
            raise InvalidAmountError("Initial balance cannot be negative.")
        self.__balance = initial_balance

    @property
    def balance(self) -> float:
        return self.__balance

    @balance.setter
    def balance(self, value: float):
        if value < 0:
            raise InvalidAmountError("Balance cannot be negative.")
        self.__balance = value

    @log_transaction
    def deposit(self, amount: float) -> float:
        if amount <= 0:
            raise InvalidAmountError("Deposit amount must be greater than zero.")
        self.__balance += amount
        return self.__balance

    @log_transaction
    def withdraw(self, amount: float) -> float:
        if amount <= 0:
            raise InvalidAmountError("Withdrawal amount must be greater than zero.")
        if amount > self.__balance:
            raise InsufficientFundsError("Insufficient funds for this withdrawal.")
        self.__balance -= amount
        return self.__balance

    def __str__(self) -> str:
        return f"BankAccount(Account: {self.account_number}, Owner: {self.owner}, Balance: {self.__balance})"

    def __eq__(self, other):
        if isinstance(other, BankAccount):
            return self.account_number == other.account_number
        return False

    def __add__(self, other):
        if isinstance(other, BankAccount):
            return self.balance + other.balance
        raise TypeError("Addition is only supported between BankAccount instances.")

class SavingsAccount(BankAccount):
    def __init__(self, account_number: str, owner: str, initial_balance: float = 0.0, interest_rate: float = 0.05):
        super().__init__(account_number, owner, initial_balance)
        self.interest_rate =interest_rate

    @log_transaction
    def apply_interest(self) -> float:
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        return self.balance

from core.exceptions import InsufficientFundsError, InvalidAmountError
from core.models import BankAccount, SavingsAccount


def main():
    print("=== 1. Creating Accounts ===")
    acc1 = BankAccount("101", "Farbod", 1000.0)
    acc2 = BankAccount("102", "Ali", 500.0)
    savings = SavingsAccount("103", "Farbod", 2000.0, interest_rate=0.10)

    print("\n=== 2. Testing Transactions & Decorator ===")
    acc1.deposit(500.0)
    acc1.withdraw(200.0)

    print("\n=== 3. Testing Magic Methods ===")
    print(f"Account 1 Info: {acc1}")
    print(f"Is acc1 equal to acc2? {acc1 == acc2}")

    # Testing __add__
    total_balance = acc1 + acc2
    print(f"Combined Balance of acc1 & acc2: {total_balance}")

    print("\n=== 4. Testing SavingsAccount Interest ===")
    savings.apply_interest()

    print("\n=== 5. Testing Error Handling ===")
    # Test Invalid Deposit
    try:
        acc1.deposit(-50.0)
    except InvalidAmountError as e:
        print(f"Caught expected error: {e}")

    # Test Insufficient Funds
    try:
        acc2.withdraw(5000.0)
    except InsufficientFundsError as e:
        print(f"Caught expected error: {e}")


if __name__ == "__main__":
    main()
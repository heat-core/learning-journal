import threading
from core.models import BankAccount


def worker_deposit(account: BankAccount, amount: float, count: int):
    """تابعی که توسط هر ترد اجرا می‌شود و چندین بار واریز انجام می‌دهد"""
    for _ in range(count):
        account.deposit(amount)


def main():
    print("=== Testing Concurrent Transactions (Thread-Safety) ===")
    account = BankAccount("101", "Farbod", initial_balance=0.0)

    threads = []
    num_threads = 100
    deposits_per_thread = 10
    amount_per_deposit = 10.0

    # ساخت ۱۰۰ ترد هم‌زمان
    for _ in range(num_threads):
        t = threading.Thread(
            target=worker_deposit,
            args=(account, amount_per_deposit, deposits_per_thread)
        )
        threads.append(t)

    # شروع کار تردها
    for t in threads:
        t.start()

    # انتظار برای پایان کار تمام تردها
    for t in threads:
        t.join()

    expected_balance = num_threads * deposits_per_thread * amount_per_deposit
    print("\n==========================================")
    print(f"Expected Final Balance: {expected_balance}")
    print(f"Actual Final Balance:   {account.balance}")
    print("==========================================")

    if account.balance == expected_balance:
        print("SUCCESS: Thread-safety verified! No race conditions detected.")
    else:
        print("FAILURE: Race condition detected!")


if __name__ == "__main__":
    main()
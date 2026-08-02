import threading
import time
from core.models import BankAccount


def monitor_account(account: BankAccount):
    """ترد ناظر که معطل می‌ماند تا سیگنال Event صادر شود"""
    print("[MONITOR] Waiting for account balance to reach target threshold...")
    # متوقف شدن ترد بدون مصرف CPU تا زمان فراخوانی event.set()
    account.balance_event.wait()
    print(f"[MONITOR] ALERT: Target reached! Current Balance: {account.balance}")


def depositor(account: BankAccount):
    """تردی که آرام‌آرام پول واریز می‌کند"""
    for i in range(3):
        time.sleep(1)  # شبیه‌سازی وقفه بین واریزها
        print(f"\n[DEPOSITOR] Deposit step {i+1}...")
        account.deposit(2000.0)


def main():
    print("=== Testing Thread Synchronization with Event ===")
    account = BankAccount("101", "Farbod", initial_balance=0.0)

    # ساخت و شروع ترد ناظر
    t_monitor = threading.Thread(target=monitor_account, args=(account,))
    t_monitor.start()

    # ساخت و شروع ترد واریزکننده
    t_depositor = threading.Thread(target=depositor, args=(account,))
    t_depositor.start()

    t_monitor.join()
    t_depositor.join()

    print("\nSimulation Finished Successfully.")


if __name__ == "__main__":
    main()
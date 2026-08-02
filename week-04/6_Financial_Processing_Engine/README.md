# Thread-Safe Financial Processing Engine

A robust, object-oriented, and concurrent financial transaction processing engine built in Python. This project demonstrates core concepts of Advanced Python, including Encapsulation, Inheritance, Custom Decorators, Magic Methods, Context Managers, and Multi-Threading with Lock/Event synchronization.

## Features

- **Encapsulation & Validation:** Custom `BankAccount` properties with input validation and private balance tracking.
- **Custom Exceptions:** Domain-specific exceptions (`InsufficientFundsError`, `InvalidAmountError`) for clear error handling.
- **Transaction Logging Decorator:** A custom decorator (`@log_transaction`) using `functools.wraps` to log operation states and re-raise exceptions cleanly.
- **Thread-Safety:** Implemented `threading.Lock` across balance operations to prevent Race Conditions under high concurrency (verified with 100 concurrent threads).
- **Context Manager Support:** Implemented `__enter__` and `__exit__` magic methods for safe resource locking using `with` statements.
- **Thread Synchronization:** Utilized `threading.Event` to trigger real-time notifications when a target balance threshold is reached.

## Project Structure

```text
advanced_python_project/
│
├── core/
│   ├── __init__.py
│   ├── exceptions.py
│   └── models.py
│
├── utils/
│   ├── __init__.py
│   └── decorators.py
│
├── main.py
├── .gitignore
└── README.md

```
How to Run
Execute the main demonstration script:
python main.py
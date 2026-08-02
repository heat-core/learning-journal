from functools import wraps


def log_transaction(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Executing {func.__name__}...")

        try:
            result = func(*args, **kwargs)
            print(f"[LOG] {func.__name__} executed successfully.")
            return result

        except Exception as e:
            print(f"[ERROR] {func.__name__} failed with error: {e}")
            raise e

    return wrapper
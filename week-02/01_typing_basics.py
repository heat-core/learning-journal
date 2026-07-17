
def add_numbers(a: int, b: int) -> int:
    """Add two integers and return the result."""
    return a + b


def greet(name: str, age: int) -> str:
    """Return a greeting message."""
    return f"Hello {name}, you are {age} years old."


if __name__ == "__main__":
    result = add_numbers(5, 3)
    print(f"5 + 3 = {result}")

    message = greet("Farbod", 32)
    print(message)
def decorator_builder(validator):

    def actual_decorator(func):

        def wrapper(*args, **kwargs):
            if validator(*args, **kwargs):
                return func(*args, **kwargs)
            return "error"

        return wrapper

    return actual_decorator

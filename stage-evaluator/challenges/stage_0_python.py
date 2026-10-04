"""
Stage 0 Challenge: Advanced Python & Systems Reliability
Gate 0 Focus: Metaclasses, Generators, Decorators, Typing & Async Concepts
"""
import time
import functools
from typing import Callable, Any, Generator, List, TypeVar

T = TypeVar("T")

def retry_with_backoff(max_retries: int = 3, base_delay: float = 0.05, backoff_factor: float = 2.0, exceptions=(Exception,)):
    """
    Decorator that retries a function upon specified exceptions using exponential backoff.
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            delay = base_delay
            last_err = None
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_err = e
                    if attempt == max_retries - 1:
                        raise
                    time.sleep(delay)
                    delay *= backoff_factor
            if last_err:
                raise last_err
        return wrapper
    return decorator


class TypedBatchPipeline:
    """
    A pipeline batcher that streams items and groups them into batches of max_size.
    Supports context management and clean iteration.
    """
    def __init__(self, max_batch_size: int = 3):
        if max_batch_size < 1:
            raise ValueError("Batch size must be at least 1")
        self.max_batch_size = max_batch_size
        self._items = []

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._items.clear()

    def batch(self, stream: Generator[T, None, None]) -> Generator[List[T], None, None]:
        batch = []
        for item in stream:
            batch.append(item)
            if len(batch) >= self.max_batch_size:
                yield list(batch)
                batch.clear()
        if batch:
            yield list(batch)


class ImmutableDataModel:
    """
    Simulates a strictly typed, immutable record with schema validation and slot memory savings.
    """
    __slots__ = ("id", "name", "score", "_frozen")

    def __init__(self, id: int, name: str, score: float):
        if not isinstance(id, int) or id <= 0:
            raise ValueError("ID must be a positive integer")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string")
        if not isinstance(score, (int, float)) or not (0.0 <= score <= 100.0):
            raise ValueError("Score must be between 0.0 and 100.0")

        object.__setattr__(self, "id", id)
        object.__setattr__(self, "name", name.strip())
        object.__setattr__(self, "score", float(score))
        object.__setattr__(self, "_frozen", True)

    def __setattr__(self, key, value):
        if getattr(self, "_frozen", False):
            raise AttributeError("ImmutableDataModel is immutable and cannot be modified")
        super().__setattr__(key, value)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "score": self.score}

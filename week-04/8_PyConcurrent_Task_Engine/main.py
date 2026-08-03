import time
from curses import wrapper


class TaskExecutionError(Exception):
    pass

class Task():
    def __init__(self, task_id: int, priority: int = 1):
        self.task_id = task_id
        self.priority = priority
        self._status = "PENDING"

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        allowed_statuses = ["PENDING", "RUNNING", "COMPLETED", "FAILED"]
        if value not in allowed_statuses:
            raise TaskExecutionError(f"Invalid status: {value}. Must be one of {allowed_statuses}")
        self._status = value


    def execute(self):
        raise NotImplementedError("Subclasses must implement execute() method.")


class DataProcessingTask(Task):
    def __init__(self, task_id: int, priority: int = 1, data: list[int] = None):
        super().__init__(task_id, priority)
        self.data = data if data is not None else []
        self.result = None
        self._status = "PENDING"

    @time_logger
    def execute(self):
        self._status = "RUNNING"
        self.result = sum(self.data)
        self._status = "COMPLETED"
        return self.result



class LoggerMixin():
    def log(self, message: str):
        print(f"[LOG]: {message}")


class LoggedNetworkTask(Task, LoggerMixin):
    def __init__(self, task_id, priority, url: str):
        super().__init__(task_id, priority)
        self.url =url
        self.result = None

    @time_logger
    def execute(self):
        self._status = "RUNNING"
        self.log(f"Connecting to {self.url}...")
        time.sleep(1)
        self.result = 200
        self._status = "COMPLETED"
        return self.result


def time_logger(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"[TIMER] Execution time for {func.__name__}: {end_time - start_time:.4f}s")
        return result
    return wrapper



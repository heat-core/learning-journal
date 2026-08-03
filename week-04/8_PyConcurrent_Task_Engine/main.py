import time

def time_logger(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"[TIMER] Execution time for {func.__name__}: {end_time - start_time:.4f}s")
        return result
    return wrapper

def inspect_task(task_obj):
    print(f"Task Name: {type(task_obj).__name__}")
    stat = getattr(task_obj, "status")
    prio = getattr(task_obj, "priority")
    print(f"Status: {stat}")
    print(f"Priority: {prio}")
    if hasattr(task_obj, "data"):
        print(f"Data: {task_obj.data}")
    if hasattr(task_obj, "url"):
        print(f"URL: {task_obj.url}")
    public_attrs = [attr for attr in dir(task_obj) if not attr.startswith("__")]
    print(f"Public Attributes/Methods: {public_attrs}")

class TaskExecutionError(Exception):
    pass


class Task:
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
        self._status = value  # اصلاح شد: به _status مقداردهی می‌کنیم

    def execute(self):
        raise NotImplementedError("Subclasses must implement execute() method.")

    def __str__(self):
        return f"[Task {self.task_id}] Priority: {self.priority} | Status: {self.status}"

    def __call__(self, *args, **kwargs):
        return self.execute()

    def __lt__(self, other):
        return self.priority < other.priority


class DataProcessingTask(Task):
    def __init__(self, task_id: int, priority: int = 1, data: list[int] = None):
        super().__init__(task_id, priority)
        self.data = data if data is not None else []
        self.result = None

    @time_logger
    def execute(self):
        self.status = "RUNNING"
        self.result = sum(self.data)
        self.status = "COMPLETED"
        return self.result


class LoggerMixin:
    def log(self, message: str):
        print(f"[LOG]: {message}")


class LoggedNetworkTask(Task, LoggerMixin):
    def __init__(self, task_id: int, priority: int = 1, url: str = ""):
        super().__init__(task_id, priority)
        self.url = url
        self.result = None

    @time_logger
    def execute(self):
        self.status = "RUNNING"
        self.log(f"Connecting to {self.url}...")
        time.sleep(1)
        self.result = 200
        self.status = "COMPLETED"
        return self.result
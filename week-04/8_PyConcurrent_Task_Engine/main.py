

class TaskExecutionError(Exception):
    pass

class Task():
    def __init__(self, task_id: int, priority: int = 1):
        self.task_id = task_id
        self.priority = priority
        self._status = "PENDING"


    def execute(self):
        raise NotImplementedError("Subclasses must implement execute() method.")


class DataProcessingTask(Task):
    def __init__(self, task_id: int, priority: int = 1, data: list[int] = None):
        super().__init__(task_id, priority)
        self.data = data
        task.execute()
        self.result = sum(self.data)
        self._status = "COMPLETED"



class LoggerMixin():
    def log(self, message: str):
        print()



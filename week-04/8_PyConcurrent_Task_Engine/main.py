import threading
import time


# --- فاز ۲: تعریف دکوراتور ---
def time_logger(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"[TIMER] Execution time for {func.__name__}: {end_time - start_time:.4f}s")
        return result

    return wrapper


# --- فاز ۳: تابع بازرسی پویا (Introspection) ---
def inspect_task(task_obj):
    print(f"\n--- Introspection for: {type(task_obj).__name__} ---")
    print(f"Status (via getattr): {getattr(task_obj, 'status')}")
    print(f"Priority (via getattr): {getattr(task_obj, 'priority')}")

    if hasattr(task_obj, "data"):
        print(f"Data attribute: {task_obj.data}")
    if hasattr(task_obj, "url"):
        print(f"URL attribute: {task_obj.url}")

    public_attrs = [attr for attr in dir(task_obj) if not attr.startswith("__")]
    print(f"Public Methods/Attrs: {public_attrs}")
    print("-" * 45)


# --- فاز ۱: استثنا و کلاس پایه ---
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
        self._status = value

    def execute(self):
        raise NotImplementedError("Subclasses must implement execute() method.")

    def __str__(self):
        return f"[Task {self.task_id}] Priority: {self.priority} | Status: {self.status}"

    def __call__(self, *args, **kwargs):
        return self.execute()

    def __lt__(self, other):
        return self.priority < other.priority


# --- کلاس‌های مشتق‌شده ---
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


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.total_processed_count = 0
        self.lock = threading.Lock()
        self.start_signal = threading.Event()

    def add_task(self, task: Task):
        self.tasks.append(task)

    def _worker(self, task: Task):
        # ۱. منتظر بمان تا سیگنال شلیک شود
        self.start_signal.wait()

        try:
            # ۲. اجرای تاسک
            task()
            # ۳. به‌روزرسانی منبع مشترک با قفل برای جلوگیری از Race Condition
            with self.lock:
                self.total_processed_count += 1
        except Exception as e:
            task.status = "FAILED"
            print(f"[ERROR] Task {task.task_id} failed: {e}")

    def run_all(self):
        threads = []

        # گام اول: ساخت و استارت زدن همه تردها (همگی منتظر سیگنال می‌مانند)
        for task in self.tasks:
            t = threading.Thread(target=self._worker, args=(task,))
            threads.append(t)
            t.start()

        print("\n[MANAGER] Starting all threads simultaneously...")
        # گام دوم: انتشار سیگنال برای شروع هم‌زمان تردها
        self.start_signal.set()

        # گام سوم: انتظار برای اتمام تمامی تردها
        for t in threads:
            t.join()

        print(f"[MANAGER] All tasks executed. Total successful tasks: {self.total_processed_count}\n")


# ==========================================
# بخش تست و بررسی رفتار کلاس‌ها
# ==========================================
if __name__ == "__main__":
    print("=== ۱. ساخت اشیاء (Instances) ===")
    t1 = DataProcessingTask(task_id=101, priority=2, data=[10, 20, 30])
    t2 = LoggedNetworkTask(task_id=102, priority=1, url="https://api.example.com")

    print("\n=== ۲. تست Dunder Methods (__str__ & __lt__) ===")
    # تست __str__: چاپ خوانای شیء
    print("t1 status:", t1)
    print("t2 status:", t2)
    # تست __lt__: مقایسه بر اساس priority (اولویت ۱ کمتر/بالاتر از اولویت ۲)
    print(f"Is t2 higher priority than t1? (t2 < t1): {t2 < t1}")

    print("\n=== ۳. تست Introspection (قبل از اجرا) ===")
    inspect_task(t1)

    print("\n=== ۴. تست اجرا با __call__ و Decorator ===")
    # فراخوانی t1() مستقیماً متد execute() را با دکوراتور time_logger اجرا می‌کند
    res1 = t1()
    print(f"DataProcessingTask Result: {res1}")

    res2 = t2()
    print(f"LoggedNetworkTask Result: {res2}")

    print("\n=== ۵. تست Validation در @status.setter ===")
    try:
        t1.status = "INVALID_STATUS"
    except TaskExecutionError as e:
        print(f"Caught expected error successfully: {e}")

    print("\n=== ۶. وضعیت نهایی اشیاء ===")
    print("t1 final state:", t1)
    print("t2 final state:", t2)

    if __name__ == "__main__":
        manager = TaskManager()
        print("\n\n\n","=== ۱. ساخت اشیاء (Start Manager) ===")

        # ساخت چند نمونه تاسک
        t1 = DataProcessingTask(task_id=1, priority=2, data=[10, 20, 30, 40])
        t2 = LoggedNetworkTask(task_id=2, priority=1, url="https://api.github.com")
        t3 = DataProcessingTask(task_id=3, priority=3, data=[1, 2, 3])
        t4 = LoggedNetworkTask(task_id=4, priority=1, url="https://python.org")

        # اضافه کردن به مدیر تاسک‌ها
        manager.add_task(t1)
        manager.add_task(t2)
        manager.add_task(t3)
        manager.add_task(t4)

        # تست بازرسی پویا روی یکی از تاسک‌ها
        inspect_task(t2)

        # اجرای هم‌زمان همه تاسک‌ها
        manager.run_all()

        # چاپ وضعیت نهایی تاسک‌ها
        print("=== Final Tasks Status ===")
        for task in manager.tasks:
            print(task)
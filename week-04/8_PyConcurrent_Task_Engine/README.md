# PyConcurrent Task Engine

## Description
`PyConcurrent Task Engine` is a lightweight, concurrent task processing framework built in Python. It demonstrates core and advanced Object-Oriented Programming (OOP) concepts, Dynamic Introspection, Decorators, and Threading synchronization primitives (Lock and Event).

## Project Architecture

### 1. OOP Core & Exception Handling
- **`Task` (Abstract Base Class)**: Defines the base properties (`task_id`, `status`, `result`) and abstract `execute()` method.
- **Subclasses**:
  - `DataProcessingTask`: Handles numerical transformations.
  - `NetworkTask`: Simulates network operations.
  - `LoggedNetworkTask`: Uses multiple inheritance with a `LoggerMixin`.
- **Custom Exceptions**:
  - `TaskExecutionError`: Raised during runtime execution failures.
  - `InvalidTaskDataError`: Raised on invalid task initialization data.

### 2. Advanced OOP Features
- **Encapsulation**: Encapsulated state management using `@property` decorators.
- **Magic (Dunder) Methods**:
  - `__str__` / `__repr__`: String representation of objects.
  - `__call__`: Enables direct execution via `task_instance()`.
  - `__lt__`: Allows task ordering and prioritization.
- **Decorators**:
  - `@time_logger`: Measures and logs function execution time.
  - `@validate_types`: Validates function argument types dynamically.
- **Introspection & Reflection**:
  - `inspect_task(task)`: Inspects task properties, methods, and types using `getattr`, `hasattr`, and `type`.

### 3. Concurrency & Threading
- **`TaskManager`**: Manages execution queues and dispatches worker threads.
- **Synchronization**:
  - **`threading.Lock`**: Protects shared state (`total_processed_count`) against race conditions.
  - **`threading.Event`**: Coordinates synchronized execution start across all worker threads.

## Installation & Setup
```bash
git clone [https://github.com/username/PyConcurrent-Task-Engine.git](https://github.com/username/PyConcurrent-Task-Engine.git)
cd PyConcurrent-Task-Engine
python main.py
```
---

## ۳. نقشه راه و سناریوی پیاده‌سازی کد (تمرین گام‌به‌گام)

کد اصلی خود را در یک فایل به نام `main.py` پیاده‌سازی کنید. نیازمندی‌های جزئی هر بخش به شرح زیر است:

### فاز ۱: پایه شی‌گرایی (OOP Base)

1. **کلاس استثنا:** 
   * کلاس `TaskExecutionError(Exception)` را بسازید.
2. **کلاس پایه `Task`:**
   * در `__init__` مقدار `task_id` و `priority` را دریافت کنید.
   * ویژگی `_status` را روی `"PENDING"` بگذارید.
   * یک متد `execute()` تعریف کنید که اگر در کلاس فرزند اوورراید نشد، `NotImplementedError` بدهد.
3. **کلاس‌های فرزند:**
   * **`DataProcessingTask`**: در متد `execute()` یک لیست از اعداد را دریافت کرده و مجموع آن‌ها را محاسبه کند.
   * **`LoggerMixin`**: یک کلاس ساده که متد `log(message)` دارد.
   * **`LoggedNetworkTask`**: ارث‌بری هم‌زمان از `Task` و `LoggerMixin`. متد `execute()` آن با `time.sleep(1)` یک درخواست شبکه را شبیه‌سازی کند.

---

### فاز ۲: قابلیت‌های متقدم (Advanced OOP)

1. **کنترل ویژگی‌ها با `@property`:**
   * برای `status` یک Property بنویسید. در `setter` بررسی کنید اگر وضعیت در لیست `["PENDING", "RUNNING", "COMPLETED", "FAILED"]` نبود، استثنا بدهد.
2. **Dunder Methods:**
   * `__call__`: فراخوانی مستقیم شیء (مثلاً `task()`) باید متد `execute()` را اجرا کند.
   * `__lt__`: مقایسه دو task بر اساس priority (برای مرتب‌سازی).
   * `__str__`: خروجی تمیز مانند `[Task 101] Status: COMPLETED`.
3. **دکوراتور `@time_logger`:**
   * دکوراتوری بنویسید که قبل و بعد از اجرای `execute()`، زمان را اندازه گرفته و مدت زمان اجرا را چاپ کند.

---

### فاز ۳: بازرسی پویا (Introspection)

1. **تابع `inspect_task(task_obj)` را بنویسید:**
   * با استفاده از `type(task_obj).__name__` نام کلاس را چاپ کند.
   * با استفاده از `dir(task_obj)` تمام متدها و ویژگی‌های شیء را پیمایش کند.
   * بررسی کند آیا ویژگی `status` وجود دارد (`hasattr`) و مقدار آن چیست (`getattr`).

---

### فاز ۴: همروندی و مدیریت تردها (Concurrency)

1. **کلاس `TaskManager`:**
   * شامل یک لیست از taskها باشد.
   * یک متغیر کلاس یا ویژگی به نام `shared_counter = 0` داشته باشد.
   * یک `threading.Lock()` برای محافظت از `shared_counter` ایجاد کنید.
   * یک `threading.Event()` به نام `start_signal` بسازید.
2. **ورکر ترد (Worker Thread Function):**
   * تردها ابتدا منتظر سیگنال بمانند: `start_signal.wait()`.
   * سپس `task.execute()` را صدا بزنند.
   * بعد از اتمام، با استفاده از `with lock:` مقدار `shared_counter` را یک واحد افزایش دهند.
3. **متد `run_all()`:**
   * برای هر task یک `threading.Thread` بسازید و `start()` کنید.
   * سپس سیگنال شروع را ارسال کنید: `start_signal.set()`.
   * با `join()` منتظر بمانید تا تمام تردها کارشان تمام شود.

---

## روش شروع کار

1. یک پوشه جدید بسازید.
2. فایل `README.md` را با محتوای بالا ایجاد کنید.
3. فایل `main.py` را بسازید و **فاز به فاز** شروع به نوشتن کد کنید.
4. هر جایی که در ساختار کلاس‌ها، قفل‌ها (Lock) یا جزییات پایتون به ابهام خوردید، کد آن بخش را بفرستید تا رفع اشکال و بهینه‌سازی کنیم.
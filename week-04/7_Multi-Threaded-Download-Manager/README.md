# Multi-Threaded Download Manager

A high-performance, object-oriented, and concurrent download manager built in Python. This project demonstrates core concepts of Advanced Python, including Encapsulation, Custom Decorators with Arguments, Magic Methods, Context Managers, and Multi-Threading with Lock/Event synchronization for parallel chunk downloads.

## Features

- **Chunked Parallel Downloading:** Splits files into multiple chunks and downloads them concurrently using Python's `threading` module.
- **Thread-Safety & Progress Tracking:** Uses `threading.Lock` to update real-time download progress and speeds without Race Conditions.
- **Custom Decorators:** Implements `@retry_on_failure(retries=3, delay=1)` to automatically handle network drops and retry chunk downloads.
- **Safe File Merging (Context Manager):** Uses custom `__enter__` and `__exit__` magic methods to ensure downloaded chunks are safely merged into the final file without corruption.
- **Custom Exceptions:** Domain-specific exceptions (`DownloadError`, `ChunkMergeError`) for clear error boundaries.

## Project Structure

```text
download_manager/
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


##  How to Run
Execute the main demonstration script:
python main.py
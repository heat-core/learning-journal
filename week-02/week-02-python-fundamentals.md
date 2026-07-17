# Week 2 — Python Fundamentals

## Type Hints
- Functions can declare expected types: `def add(a: int, b: int) -> int`
- Doesn't enforce at runtime, but helps IDE/tools catch bugs early.

## Dataclasses
- `@dataclass` auto-generates `__init__`, `__repr__`, etc.
- Gotcha: mutable defaults (like lists) must use `field(default_factory=list)`,
  otherwise all instances share the same list — classic Python bug.

## Questions/Confusions
- (whatever you're unsure about)
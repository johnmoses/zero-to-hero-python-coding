# Concurrency

Concurrency allows a program to handle multiple tasks at the same time. Python provides three main approaches.

## Threading

Best for I/O-bound tasks (network calls, file reads). Threads share memory.

```py
import threading

def task(name):
    print(f"Task {name} running")

t1 = threading.Thread(target=task, args=("A",))
t2 = threading.Thread(target=task, args=("B",))
t1.start()
t2.start()
t1.join()
t2.join()
```

## Multiprocessing

Best for CPU-bound tasks. Each process has its own memory space, bypassing the GIL.

```py
from multiprocessing import Process

def task(name):
    print(f"Process {name} running")

p = Process(target=task, args=("A",))
p.start()
p.join()
```

## Asyncio

Best for high-concurrency I/O (APIs, websockets). Uses a single thread with an event loop.

```py
import asyncio

async def task(name):
    await asyncio.sleep(1)
    print(f"Task {name} done")

async def main():
    await asyncio.gather(task("A"), task("B"))

asyncio.run(main())
```

## When to use what

| Scenario | Approach |
|----------|----------|
| File/network I/O | threading or asyncio |
| CPU-heavy computation | multiprocessing |
| Many concurrent connections | asyncio |

# Multi-Threading

This directory contains examples and demonstrations of multi-threading implementations in Python.

## Files

### [create_threads.py](file:///D:/distributed-crawler/lld/multi-threading/create_threads.py)
This script demonstrates the fundamentals of thread management using Python's built-in `threading` module.

#### What it covers:
- Creating and starting basic threads ([`func`](file:///D:/distributed-crawler/lld/multi-threading/create_threads.py#L5)) using `threading.Thread`.
- Passing arguments to threaded functions ([`func_with_arg`](file:///D:/distributed-crawler/lld/multi-threading/create_threads.py#L8)) using tuples.
- Spawning multiple threads concurrently in a loop and waiting for all of them to finish using `join()`.

#### Recent Improvements:
- **Pythonic Loop Refactoring:** Simplified how threads are stored and started in the spawning loop.
- **Argument Conventions:** Updated thread arguments to use standard tuples `args=(i,)` instead of lists.
- **Typo Fixes:** Corrected spelling of `argument` across print statements and comments.

---

### [locks.py](file:///D:/distributed-crawler/lld/multi-threading/locks.py)
Demonstrates the hazard of **race conditions** on shared global state when multiple threads write to the same variable simultaneously, and how to resolve it with locks.

#### What it covers:
- Simulating a race condition via [`race_condition_demo`](file:///D:/distributed-crawler/lld/multi-threading/locks.py#L12) where increments are lost due to interleaving thread executions.
- Resolving the issue with mutual exclusion using `threading.Lock` inside [`demo_with_lock`](file:///D:/distributed-crawler/lld/multi-threading/locks.py#L28).
- Measuring and comparing performance, illustrating how lock acquisition overhead increases execution time.

---

### [print_even_odd_with_locks.py](file:///D:/distributed-crawler/lld/multi-threading/print_even_odd_with_locks.py)
Uses a shared `threading.Lock` to coordinate two threads so they print even and odd numbers in alternating order.

#### Recent Improvements:
- **Boundary Race Condition Fix:** Moved the boundary condition check inside the lock (`if num > total_num: break`) to prevent threads from racing and printing past the limit of `total_num`.
- **Proper Thread Cleanup:** Added explicit `t1.join()` and `t2.join()` in [`main`](file:///D:/distributed-crawler/lld/multi-threading/print_even_odd_with_locks.py#L25) to block the main thread until work is completed.
- **Formatting:** Standardized double indentation.

---

### [conditionals.py](file:///D:/distributed-crawler/lld/multi-threading/conditionals.py)
Shows a more efficient way to synchronize alternating threads using condition variables (`threading.Condition`), avoiding the busy-waiting (spinning) overhead of standard locks.

#### Key Features:
- Threads release the lock and enter a sleeping state using `cv.wait()` when it is not their turn.
- Active threads notify sleeping threads using `cv.notify()` after updating the state.

#### Recent Improvements:
- **Boundary Bug Fix:** Corrected a boundary condition where `odd thread printing 101` was printed (exceeding `mx = 100`). Checking the loop state inside the lock block (`while num % 2 and num <= mx: cv.wait()`) and checking `if num > mx: break` ensures both threads exit cleanly without extra output.

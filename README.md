# Low-Level Design (LLD) Patterns in Python

This repository contains clean, standard Python implementations of classic Gang of Four (GoF) design patterns and core concurrency patterns. Each pattern directory includes production-grade source code, thorough docstrings, and a comprehensive **Learning & Revision Guide** complete with UML diagrams, real-world analogies, code walkthroughs, trade-off cheat sheets, and frequently asked interview questions.

---

## 🛠️ Table of Patterns

### 1. Creational Patterns
Creational design patterns provide various object creation mechanisms, which increase flexibility and reuse of existing code.

| Pattern | Description & Documentation | Implementation Entry Point |
| :--- | :--- | :--- |
| 🏗️ **Builder** | [Builder Guide](file:///D:/distributed-crawler/lld/creational/builder/README.md) <br> Construct complex objects step-by-step with clean method chaining. | [creational/builder/main.py](file:///D:/distributed-crawler/lld/creational/builder/main.py) |
| 🏭 **Factory** | [Factory Guide](file:///D:/distributed-crawler/lld/creational/factory/README.md) <br> Encapsulate object creation logic, decoupling clients from concrete classes. | [creational/factory/DBfactory.py](file:///D:/distributed-crawler/lld/creational/factory/DBfactory.py) |
| 🏛️ **Abstract Factory** | [Abstract Factory Guide](file:///D:/distributed-crawler/lld/creational/abstract%20factory/README.md) <br> Produce families of related or dependent objects without specifying concrete classes. | [creational/abstract factory/main.py](file:///D:/distributed-crawler/lld/creational/abstract%20factory/main.py) |
| 👤 **Singleton** | [Singleton Guide](file:///D:/distributed-crawler/lld/creational/singleton/README.md) <br> Ensure a class has only one instance with double-checked locking and initialization guards. | [creational/singleton/logger.py](file:///D:/distributed-crawler/lld/creational/singleton/logger.py) <br> [creational/singleton/other_way.py](file:///D:/distributed-crawler/lld/creational/singleton/other_way.py) |

---

### 2. Structural Patterns
Structural design patterns explain how to assemble objects and classes into larger structures while keeping these structures flexible and efficient.

| Pattern | Description & Documentation | Implementation Entry Point |
| :--- | :--- | :--- |
| 🔌 **Adapter** | [Adapter Guide](file:///D:/distributed-crawler/lld/structural/adapter/README.md) <br> Allow objects with incompatible interfaces to collaborate seamlessly via object composition. | [structural/adapter/adapter.py](file:///D:/distributed-crawler/lld/structural/adapter/adapter.py) |
| ☕ **Decorator** | [Decorator Guide](file:///D:/distributed-crawler/lld/structural/decorator/README.md) <br> Attach new responsibilities and behaviors to objects dynamically without altering original classes. | [structural/decorator/decorator.py](file:///D:/distributed-crawler/lld/structural/decorator/decorator.py) |

---

### 3. Behavioral Patterns
Behavioral design patterns are concerned with algorithms and the assignment of responsibilities between objects.

| Pattern | Description & Documentation | Implementation Entry Point |
| :--- | :--- | :--- |
| 🔗 **Chain of Responsibility** | [Chain of Responsibility Guide](file:///D:/distributed-crawler/lld/behavioral/chain%20of%20responsibility/README.md) <br> Pass requests along a dynamic chain of handlers until one processes it. | [behavioral/chain of responsibility/main.py](file:///D:/distributed-crawler/lld/behavioral/chain%20of%20responsibility/main.py) |
| 📜 **Command** | [Command Guide](file:///D:/distributed-crawler/lld/behavioral/command/README.md) <br> Encapsulate requests as standalone objects to support parameterization, queues, and undo operations. | [behavioral/command/main.py](file:///D:/distributed-crawler/lld/behavioral/command/main.py) |
| 🔄 **Iterator** | [Iterator Guide](file:///D:/distributed-crawler/lld/behavioral/iterator/README.md) <br> Sequentially traverse elements of a complex collection without exposing its underlying representation. | [behavioral/iterator/main.py](file:///D:/distributed-crawler/lld/behavioral/iterator/main.py) |
| 🔔 **Observer** | [Observer Guide](file:///D:/distributed-crawler/lld/behavioral/observer/README.md) <br> Establish a thread-safe publish-subscribe broadcast mechanism between subjects and observers. | [behavioral/observer/main.py](file:///D:/distributed-crawler/lld/behavioral/observer/main.py) |
| 🎯 **Strategy** | [Strategy Guide](file:///D:/distributed-crawler/lld/behavioral/strategy/README.md) <br> Define a family of interchangeable algorithms, enabling clients to choose behavior dynamically at runtime. | [behavioral/strategy/main.py](file:///D:/distributed-crawler/lld/behavioral/strategy/main.py) |
| 📐 **Template Method** | [Template Method Guide](file:///D:/distributed-crawler/lld/behavioral/template/README.md) <br> Define algorithm skeletons in a superclass, letting subclasses override specific steps without changing the structure. | [behavioral/template/template.py](file:///D:/distributed-crawler/lld/behavioral/template/template.py) |

---

### 4. Concurrency & Multi-Threading
Core multi-threading patterns and synchronization primitives for low-level concurrent system design.

| Module | Description & Documentation | Implementation Entry Point |
| :--- | :--- | :--- |
| 🧵 **Multi-Threading** | [Multi-Threading Guide](file:///D:/distributed-crawler/lld/multi-threading/README.md) <br> Thread lifecycles, race condition avoidance via locks, condition variables, and producer-consumer queue. | [multi-threading/prod_cons.py](file:///D:/distributed-crawler/lld/multi-threading/prod_cons.py) <br> [multi-threading/locks.py](file:///D:/distributed-crawler/lld/multi-threading/locks.py) |

---

## 🎯 Low-Level System Design Practice Problems

Located in the [`practise/`](file:///D:/distributed-crawler/lld/practise) directory:
- 🅿️ **Parking Lot**: Multi-level parking lot system modeling vehicles, parking spots, pricing strategies, and ticket lifecycles.
- ⭕❌ **Tic-Tac-Toe**: Configurable n-size board game leveraging the Builder and Strategy design patterns.

---

## 🚀 How to Run the Patterns

Each pattern contains a standalone executable demonstration. Run any script from the workspace root:

```bash
# Creational Patterns
python creational/builder/main.py
python creational/factory/DBfactory.py
python "creational/abstract factory/main.py"
python creational/singleton/logger.py
python creational/singleton/other_way.py

# Structural Patterns
python structural/adapter/adapter.py
python structural/decorator/decorator.py

# Behavioral Patterns
python "behavioral/chain of responsibility/main.py"
python behavioral/command/main.py
python behavioral/iterator/main.py
python behavioral/observer/main.py
python behavioral/strategy/main.py
python behavioral/template/template.py

# Multi-Threading Demonstrations
python multi-threading/create_threads.py
python multi-threading/locks.py
python multi-threading/print_even_odd_with_locks.py
python multi-threading/conditionals.py
python multi-threading/prod_cons.py
```
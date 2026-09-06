# Low-Level Design (LLD) Patterns in Python

This repository contains clean, standard Python implementations of classic Gang of Four (GoF) design patterns and core concurrency patterns. Each pattern directory includes production-grade source code, thorough docstrings, and a comprehensive **Learning & Revision Guide** complete with UML diagrams, real-world analogies, code walkthroughs, trade-off cheat sheets, and frequently asked interview questions.

---

## 🛠️ Table of Patterns

### 1. Creational Patterns
Creational design patterns provide various object creation mechanisms, which increase flexibility and reuse of existing code.

| Pattern | Description & Documentation | Implementation Entry Point |
| :--- | :--- | :--- |
| 🏗️ **Builder** | [Builder Guide](file:///D:/distributed-crawler/lld/builder/README.md) <br> Construct complex objects step-by-step with clean method chaining. | [builder/main.py](file:///D:/distributed-crawler/lld/builder/main.py) |
| 🏭 **Factory** | [Factory Guide](file:///D:/distributed-crawler/lld/factory/README.md) <br> Encapsulate object creation logic, decoupling clients from concrete classes. | [factory/DBfactory.py](file:///D:/distributed-crawler/lld/factory/DBfactory.py) |
| 🏛️ **Abstract Factory** | [Abstract Factory Guide](file:///D:/distributed-crawler/lld/abstract%20factory/README.md) <br> Produce families of related or dependent objects without specifying concrete classes. | [abstract factory/main.py](file:///D:/distributed-crawler/lld/abstract%20factory/main.py) |
| 👤 **Singleton** | [Singleton Guide](file:///D:/distributed-crawler/lld/singleton/README.md) <br> Ensure a class has only one instance with double-checked locking and initialization guards. | [singleton/logger.py](file:///D:/distributed-crawler/lld/singleton/logger.py) <br> [singleton/other_way.py](file:///D:/distributed-crawler/lld/singleton/other_way.py) |

---

### 2. Structural Patterns
Structural design patterns explain how to assemble objects and classes into larger structures while keeping these structures flexible and efficient.

| Pattern | Description & Documentation | Implementation Entry Point |
| :--- | :--- | :--- |
| 🔌 **Adapter** | [Adapter Guide](file:///D:/distributed-crawler/lld/adapter/README.md) <br> Allow objects with incompatible interfaces to collaborate seamlessly via object composition. | [adapter/adapter.py](file:///D:/distributed-crawler/lld/adapter/adapter.py) |
| ☕ **Decorator** | [Decorator Guide](file:///D:/distributed-crawler/lld/decorator/README.md) <br> Attach new responsibilities and behaviors to objects dynamically without altering original classes. | [decorator/decorator.py](file:///D:/distributed-crawler/lld/decorator/decorator.py) |

---

### 3. Behavioral Patterns
Behavioral design patterns are concerned with algorithms and the assignment of responsibilities between objects.

| Pattern | Description & Documentation | Implementation Entry Point |
| :--- | :--- | :--- |
| 🔗 **Chain of Responsibility** | [Chain of Responsibility Guide](file:///D:/distributed-crawler/lld/chain%20of%20responsibility/README.md) <br> Pass requests along a dynamic chain of handlers until one processes it. | [chain of responsibility/main.py](file:///D:/distributed-crawler/lld/chain%20of%20responsibility/main.py) |
| 📜 **Command** | [Command Guide](file:///D:/distributed-crawler/lld/command/README.md) <br> Encapsulate requests as standalone objects to support parameterization, queues, and undo operations. | [command/main.py](file:///D:/distributed-crawler/lld/command/main.py) |
| 🔄 **Iterator** | [Iterator Guide](file:///D:/distributed-crawler/lld/iterator/README.md) <br> Sequentially traverse elements of a complex collection without exposing its underlying representation. | [iterator/main.py](file:///D:/distributed-crawler/lld/iterator/main.py) |
| 🔔 **Observer** | [Observer Guide](file:///D:/distributed-crawler/lld/observer/README.md) <br> Establish a thread-safe publish-subscribe broadcast mechanism between subjects and observers. | [observer/main.py](file:///D:/distributed-crawler/lld/observer/main.py) |
| 🎯 **Strategy** | [Strategy Guide](file:///D:/distributed-crawler/lld/strategy/README.md) <br> Define a family of interchangeable algorithms, enabling clients to choose behavior dynamically at runtime. | [strategy/main.py](file:///D:/distributed-crawler/lld/strategy/main.py) |
| 📐 **Template Method** | [Template Method Guide](file:///D:/distributed-crawler/lld/template/README.md) <br> Define algorithm skeletons in a superclass, letting subclasses override specific steps without changing the structure. | [template/template.py](file:///D:/distributed-crawler/lld/template/template.py) |

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
python builder/main.py
python factory/DBfactory.py
python "abstract factory/main.py"
python singleton/logger.py
python singleton/other_way.py

# Structural Patterns
python adapter/adapter.py
python decorator/decorator.py

# Behavioral Patterns
python "chain of responsibility/main.py"
python command/main.py
python iterator/main.py
python observer/main.py
python strategy/main.py
python template/template.py

# Multi-Threading Demonstrations
python multi-threading/create_threads.py
python multi-threading/locks.py
python multi-threading/print_even_odd_with_locks.py
python multi-threading/conditionals.py
python multi-threading/prod_cons.py
```
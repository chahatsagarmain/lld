# Low-Level Design (LLD) Patterns in Python

This repository contains clean, standard Python implementations of various classic design patterns. It serves as a practical reference guide for understanding low-level system design concepts.

---

## 🛠️ Table of Patterns

| Pattern Category | Design Pattern | Description & Documentation | Implementation Entry Point |
| :--- | :--- | :--- | :--- |
| **Creational** | 🏗️ [Builder](file:///D:/distributed-crawler/lld/builder/README.md) | Construct complex objects step-by-step with clean method chaining. | [builder/main.py](file:///D:/distributed-crawler/lld/builder/main.py) |
| **Creational** | 🏭 [Factory](file:///D:/distributed-crawler/lld/factory/README.md) | Define interfaces for creating objects, delegating instantiation logic to subclasses. | [factory/DBfactory.py](file:///D:/distributed-crawler/lld/factory/DBfactory.py) |
| **Creational** | 🏛️ [Abstract Factory](file:///D:/distributed-crawler/lld/abstract_factory/README.md) | Produce families of related or dependent objects without specifying their concrete classes. | [abstract_factory/main.py](file:///D:/distributed-crawler/lld/abstract_factory/main.py) |
| **Creational** | 👤 [Singleton](file:///D:/distributed-crawler/lld/singleton/README.md) | Ensure a class has only one instance and provide a global point of access. | [singleton/logger.py](file:///D:/distributed-crawler/lld/singleton/logger.py) |
| **Behavioral** | 📜 [Command](file:///D:/distributed-crawler/lld/command/README.md) | Encapsulate requests or actions as objects to support parameterization, queues, and undo operations. | [command/main.py](file:///D:/distributed-crawler/lld/command/main.py) |
| **Behavioral** | 🔄 [Iterator](file:///D:/distributed-crawler/lld/iterator/README.md) | Traverse elements of a collection without exposing its underlying representation. | [iterator/main.py](file:///D:/distributed-crawler/lld/iterator/main.py) |
| **Behavioral** | 🔔 [Observer](file:///D:/distributed-crawler/lld/observer/README.md) | Establish a one-to-many dependency between objects so that state changes are automatically broadcast. | [observer/main.py](file:///D:/distributed-crawler/lld/observer/main.py) |
| **Behavioral** | 🎯 [Strategy](file:///D:/distributed-crawler/lld/strategy/README.md) | Define a family of interchangeable algorithms, enabling clients to choose behavior dynamically. | [strategy/main.py](file:///D:/distributed-crawler/lld/strategy/main.py) |

---

## 🚀 How to Run the Patterns

Each pattern contains a standalone `main.py` (or equivalent execution script) showcasing its functionality in action. To execute any pattern, run the python command from the workspace root:

```bash
# Example: Running the Builder pattern
python builder/main.py

# Example: Running the Command pattern
python command/main.py

# Example: Running the Strategy pattern
python strategy/main.py
```
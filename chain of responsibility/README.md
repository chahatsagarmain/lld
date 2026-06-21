# Chain of Responsibility Pattern

The **Chain of Responsibility** is a behavioral design pattern that allows you to pass requests along a chain of handlers. Upon receiving a request, each handler decides either to process the request or to pass it to the next handler in the chain.

## Structure

- **`HandlerInterface`**: An abstract base class that defines the interface for handling requests. It also implements the `set_next` method to support chaining and manages the reference to the next handler in the chain.
- **Concrete Handlers (`Handler1`, `Handler2`, `Handler3`)**: Implement the actual request processing logic. If a handler cannot handle a specific request, it delegates it to the next handler in the chain.

## Usage

Handlers can be easily chained together using method chaining:

```python
from handlers import Handler1, Handler2, Handler3

# Initialize handlers
h1 = Handler1()
h2 = Handler2()
h3 = Handler3()

# Chain them together
h1.set_next(h2).set_next(h3)

# Send requests to the start of the chain
h1.handle({"req1": 1})  # Handled by Handler1
h1.handle({"req2": 1})  # Handled by Handler2
h1.handle({"req3": 1})  # Handled by Handler3
h1.handle({"req4": 1})  # Reaches the end of the chain, remains unhandled
```

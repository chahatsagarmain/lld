# Adapter Design Pattern

The **Adapter Pattern** is a structural design pattern that allows objects with incompatible interfaces to collaborate.

For a detailed, graphic-rich study guide, see the [Adapter Pattern Revision Guide](file:///C:/Users/HP/.gemini/antigravity-cli/brain/f157d9bd-9caa-4ed7-9236-154cca9f46c5/adapter_revision_guide.md).

## Quick Summary

- **Intent**: Convert the interface of a class into another interface that clients expect.
- **Analogy**: A power plug adapter.
- **Key Principle**: Favor Composition over Inheritance (Object Adapter).

## Code Structure

In this directory, [adapter.py](file:///D:/distributed-crawler/lld/adapter/adapter.py) showcases an **Object Adapter** setup:

1. **Target Interface**: `NotificationService`
   - Defines the standard interface expected by the client: `send(self, sender, reciever, title, body)`.
2. **Concrete Implementation**: `EmailNotificationService`
   - The default in-house implementation conforming to the target interface.
3. **Adaptee**: `ThirdPartyEmailService`
   - The external service with a different interface: `send_email(self, sender, reciever, title, body, bcc, cc)`.
4. **Adapter**: `ThirdPartyEmailServiceAdapter`
   - Implements `NotificationService` (Target) and wraps `ThirdPartyEmailService` (Adaptee) to map standard parameters to the third-party's method signature.

## Running the Code

You can run the script to see the adapter in action:

```bash
python adapter.py
```

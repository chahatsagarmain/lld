from abc import ABC
import threading
from observer import Observer

class Subject(ABC):
    """
    Thread-safe Subject base class.
    Handles observer registration, removal, and notification.
    """
    def __init__(self) -> None:
        self._observers: list[Observer] = []
        self._lock = threading.Lock()

    def add_observer(self, observer: Observer) -> None:
        """Register an observer."""
        with self._lock:
            if observer not in self._observers:
                self._observers.append(observer)

    def remove_observer(self, observer: Observer) -> None:
        """Deregister an observer."""
        with self._lock:
            if observer in self._observers:
                self._observers.remove(observer)

    def notify_observers(self, signal: int) -> None:
        """Notify all registered observers. Calls receive_signal on each."""
        # Create a copy of the observers list to release the lock before
        # executing observer callbacks. This avoids potential deadlocks if
        # callbacks try to modify the observer list.
        with self._lock:
            observers_copy = list(self._observers)
        
        for observer in observers_copy:
            observer.receive_signal(signal)

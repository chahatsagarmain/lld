import threading
from subject import Subject

class Tower(Subject):
    """
    Tower represents the Subject (publisher) that broadcasts signals
    to registered receivers (observers) whenever its state changes.
    """
    def __init__(self) -> None:
        super().__init__()
        self._signal = 0
        self._signal_lock = threading.Lock()

    @property
    def signal(self) -> int:
        """Get the current signal value."""
        with self._signal_lock:
            return self._signal

    def update_signal(self) -> None:
        """
        Increment the signal value and automatically notify all observers.
        """
        with self._signal_lock:
            self._signal += 1
            current_signal = self._signal

        # Trigger notification automatically as part of the state change
        self.notify_observers(current_signal)

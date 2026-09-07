from observer import Observer

class PhoneReceiver(Observer):
    """Observer implementation representing a phone receiving signals."""
    
    def receive_signal(self, signal: int) -> None:
        print(f"Phone receiver received signal: {signal}")

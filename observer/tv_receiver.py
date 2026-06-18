from observer import Observer

class TvReceiver(Observer):
    """Observer implementation representing a TV receiving signals."""
    
    def receive_signal(self, signal: int) -> None:
        print(f"TV received signal {signal}")

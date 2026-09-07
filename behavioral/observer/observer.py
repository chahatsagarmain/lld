from abc import ABC, abstractmethod

class Observer(ABC):

    @abstractmethod
    def receive_signal(self, signal: int):
        pass